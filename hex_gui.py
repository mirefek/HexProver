#!/usr/bin/python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib
import numpy as np
import os

from hex_diagram import HexDiagram, positions_true
from load_puzzles import HexPuzzle
from goal import GoalEnv, BuildSplit, BuildCases
from save_proof import export_proof_to_file, load_proof_from_file

class StrategyViewer:
    def __init__(self, diagram):
        self.stack = []
        self.strategy = diagram.thm.strategy
        self.node_to_pos = dict()
        for node in self.strategy.nodes:
            [pos] = diagram.components[node]
            self.node_to_pos[node] = pos
        self.pos_to_node = diagram.pos_to_node
        self.shape = diagram.shape
        self.color0 = (0.2, 0.2, 0.2)
        self.color1 = (0.8, 0.8, 0.8)
        self.update()

    def move(self, blue_pos):
        blue = self.pos_to_node[blue_pos]
        red, next_strategy = self.strategy.respond(blue)
        red_pos = self.node_to_pos[red]
        self.stack.append((blue_pos, red_pos, self.strategy))
        self.strategy = next_strategy
        self.update()

    def update(self):
        self.num_classes = len(self.strategy.strategies)
        self.pos_to_class = np.zeros(self.shape, dtype = int)
        self.available = np.zeros(self.shape, dtype = bool)
        classes = sorted(
            sorted(strategy.nodes)
            for strategy in self.strategy.strategies
        )
        for cli, cl in enumerate(classes):
            for node in cl:
                pos = self.node_to_pos[node]
                self.pos_to_class[pos] = cli
                self.available[pos] = True

        r0,g0,b0 = self.color0
        r1,g1,b1 = self.color1
        rs = np.linspace(r0,r1, self.num_classes+1, endpoint = False)[1:]
        gs = np.linspace(r0,r1, self.num_classes+1, endpoint = False)[1:]
        bs = np.linspace(r0,r1, self.num_classes+1, endpoint = False)[1:]
        self.colors = list(zip(rs,gs,bs))

    def undo(self):
        if not self.stack: return False
        _,_,self.strategy = self.stack.pop()
        self.update()
        return True

class HexGUI(Gtk.Window):

    def __init__(self, diagrams, pack_name, start_level, proof_dir, auto_close_flag, win_size = (800, 600)):
        
        super(HexGUI, self).__init__()

        self.proof_dir = proof_dir
        self.pack_name = pack_name

        self.drag_tolerance = 20 # square distance in pixels to consider a click a drag
        self.diagrams = diagrams
        self.diagram_i = None
        self.auto_close_flag = auto_close_flag
        self.default_connect_up = True

        self.bg_color         = (0.9, 0.9, 0.9)
        self.solved_bg_color  = (0.7, 0.9, 0.7)
        self.red_color        = (0.8, 0.3, 0.3)
        self.blue_color       = (0.5, 0.5, 0.8)
        self.empty_color      = (0.5, 0.5, 0.5)
        self.light_color      = (0.7, 0.7, 0.7)
        self.loading_proof = False

        self.darea = Gtk.DrawingArea()
        self.darea.connect("draw", self.on_draw)
        self.set_events(Gdk.EventMask.KEY_PRESS_MASK)
        self.darea.set_events(Gdk.EventMask.BUTTON_PRESS_MASK |
                              Gdk.EventMask.BUTTON_RELEASE_MASK |
                              # Gdk.EventMask.SCROLL_MASK |
                              Gdk.EventMask.BUTTON1_MOTION_MASK )

        self.vbox = Gtk.VBox()
        self.top_bar = Gtk.HBox()
        self.level_label = Gtk.Label()
        self.button_auto = Gtk.ToggleButton(label="Automatiion")
        self.button_auto.set_active(self.auto_close_flag)
        self.button_auto_once = Gtk.Button.new_with_label(label = "run once")
        self.arrow_button = Gtk.Button()
        self.update_arrow_button()
        self.top_bar.pack_start(self.level_label, False, False, 20)
        self.top_bar.pack_end(self.button_auto_once, False, False, 0)
        self.top_bar.pack_end(self.button_auto, False, False, 0)
        self.top_bar.pack_end(self.arrow_button, False, False, 10)
        self.top_bar.pack_end(Gtk.Label(label = "First connect:"), False, False, 0)

        self.button_auto.connect("clicked", self.toggle_auto)
        self.button_auto_once.connect("clicked", self.run_auto_once)
        self.arrow_button.connect("clicked", self.toggle_default_connect)

        self.vbox.pack_start(self.top_bar, False, False, 0)
        self.vbox.add(self.darea)
        self.add(self.vbox)

        self.darea.connect("button-press-event", self.on_button_press)
        self.darea.connect("button-release-event", self.on_button_release)
        self.darea.connect("motion-notify-event", self.on_motion)
        self.connect("key-press-event", self.on_key_press)

        if start_level is None:
            diagram_i = 0
            while os.path.exists(self.get_proof_fname(diagram_i)):
                diagram_i += 1
        else:
            diagram_i = start_level-1
        self.set_level(diagram_i)

        self.set_title("Hex Puzzle")
        self.resize(*win_size)
        self.screen_border = 10
        self.scale = 50
        self.shift = (100,100)
        self.show_all()
        self.drag = None

    @property
    def diagram(self):
        if self.env.finished: return self.env.main
        else: return self.env.cur

    def update_arrow_button(self, *args):
        if self.default_connect_up:
            self.arrow_button.set_label(label = "▽")
        else:
            self.arrow_button.set_label(label = "▲")
    def toggle_auto(self, button):
        active = button.get_active()
        if active == self.auto_close_flag: return
        self.auto_close_flag = active
        if active:
            self.auto_close()
            self.update()
    def run_auto_once(self, button):
        self.env.close_with_fork() or self.env.close_with_lemma(include_red = True)
        self.update()
    def toggle_default_connect(self, button):
        self.default_connect_up = not self.default_connect_up
        self.update_arrow_button()

    def auto_close(self):
        if self.auto_close_flag:
            while self.env.close_with_fork() or self.env.close_with_lemma(include_red = False):
                pass

    def finished_trigger(self):
        self.strategy_viewer = StrategyViewer(self.diagram)
        if not self.loading_proof: self.save_proof()

    def get_steps_fname(self):
        return os.path.join(self.proof_dir, f"{self.pack_name}_{self.diagram_i+1}_steps.pkl")
    def get_proof_fname(self, diagram_i = None):
        if diagram_i is None: diagram_i = self.diagram_i
        return os.path.join(self.proof_dir, f"{self.pack_name}_{diagram_i+1}.hpf")

    def save_proof(self):
        os.makedirs(self.proof_dir, exist_ok = True)
        fname = self.get_proof_fname()
        export_proof_to_file(self.diagram.thm, fname)

    def load_proof(self):
        self.loading_proof = True
        if self.diagram.thm is not None:
            self.env._finish()
            return
        fname = self.get_proof_fname()
        if os.path.exists(fname):
            try:
                thm = load_proof_from_file(fname)
            except:
                print(f"Warning: Couldn't load proof from {fname}, corrupted file?")
                thm = None
            if thm is not None:
                if thm.clause <= self.diagram.clause:
                    self.diagram.add_theorem(thm)
                    self.env._finish()
                else:
                    print(f"Warning: Proof at {fname} is not fitting. Name clash / updated diagram?")
                    print(thm)
                    print(self.diagram.clause)
        self.loading_proof = False

    def save_steps(self):
        if not self.env.steps: return
        self.env.save_steps(self.get_steps_fname())
        print("Steps saved")
    def load_steps(self):
        if self.env.finished: return
        self.env.load_steps(self.get_steps_fname())

    def set_level(self, diagram_i):
        if diagram_i < 0: diagram_i = 0
        if diagram_i >= len(self.diagrams): diagram_i = len(self.diagrams)-1
        if diagram_i == self.diagram_i: return
        diagram = self.diagrams[diagram_i]
        label_str = f"{diagram_i+1} / {len(self.diagrams)}"
        if diagram.comments and diagram.comments[0]:
            label_str += "  --  "+diagram.comments[0]
        self.level_label.set_label(label_str)
        self.diagram_i = diagram_i
        self.strategy_viewer = None
        self.env = GoalEnv(diagram, finished_trigger = self.finished_trigger)
        proof_fname = self.get_proof_fname()
        self.load_proof()
        self.auto_close()

    def pixel_to_coor(self, pixel):
        x,y = pixel
        x_shift, y_shift = self.shift
        return (x-x_shift) / self.scale, (y-y_shift) / self.scale
    def coor_to_hex(self, coor, only_available = True):
        x,y = coor
        h = np.sqrt(3)/2
        x_base = int(np.floor(x-y/2))
        y_base = int(np.floor(y/h))
        coors = [
            ((ix+iy/2 - x)**2 + (iy*h - y)**2, (iy,ix))
            for iy in (y_base, y_base+1)
            for ix in (x_base, x_base+1)
        ]
        _, res = min(coors)
        iy,ix = res
        if only_available:
            if not (0 <= ix < self.diagram.width): return None
            if not (0 <= iy < self.diagram.height): return None
            if not self.diagram.available_mask[iy,ix]: return None
            if self.env.finished and not self.strategy_viewer.available[iy,ix]: return None
        return res
    def mouse_to_coor(self, e, only_available = True):
        return self.coor_to_hex(self.pixel_to_coor((e.x, e.y)))

    def on_button_press(self, w, e):
        if e.type != Gdk.EventType.BUTTON_PRESS: # eliminate double click
            return

        if self.drag is not None: self.update()
        pos = self.mouse_to_coor(e)
        if pos is not None:
            if self.env.finished:
                if e.button == 1:
                    self.strategy_viewer.move(pos)
                    self.update()
            else:
                if e.button == 1:
                    if not self.start_drag(e, pos):
                        self.left_click(pos)
                        self.update()
                elif e.button == 3:
                    self.right_click(pos)
                    self.update()

    def get_drag_tactic(self, pos1, pos2):
        if pos2 is None: return None
        node1 = self.diagram.pos_to_node[pos1]
        node2 = self.diagram.pos_to_node[pos2]
        if node1 not in self.diagram.red_nodes: return None
        if node2 not in self.diagram.red_nodes: return None
        if node1 == node2: return None
        up_node = self.diagram.up_node
        down_node = self.diagram.down_node
        if node1 == up_node:
            if node2 == down_node: return None
            return lambda: self.env.split_node(pos2, first_connect_up = True)
        elif node1 == down_node:
            if node2 == up_node: return None
            return lambda: self.env.split_node(pos2, first_connect_up = False)
        elif node2 == up_node:
            return lambda: self.env.split_node(pos1, first_connect_up = True)
        elif node2 == down_node:
            return lambda: self.env.split_node(pos1, first_connect_up = False)
        else:
            if pos1[0] > pos2[0]: pos1,pos2 = pos2,pos1
            return lambda: self.env.internal_connection(pos1, pos2)

    def start_drag(self, e, pos):
        self.drag = None
        if not self.env.waiting_for_thm: return False
        if pos is None: return False
        node = self.diagram.pos_to_node[pos]
        if node not in self.diagram.red_nodes: return False
        self.drag = "click", ((e.x,e.y), pos)
        return True
    def on_button_release(self, w, e):
        if self.drag is not None:
            mode, data = self.drag
            if mode == "click":
                pixes, pos = data
                self.left_click(pos)
            elif "drag":
                pos1, coor2, tactic = data
                if tactic is not None:
                    tactic()
                    self.auto_close()
            else:
                raise Exception(f"unexpected drag mode: {mode}")
        if self.drag is not None: self.update()
    def on_motion(self, w, e):
        if self.drag is None: return
        mode, data = self.drag
        if mode == "click":
            (x,y),pos1 = data
            if (e.x-x)**2 + (e.y-y)**2 < self.drag_tolerance:
                return
        elif mode == "drag":
            pos1,coor2,tactic = data
        else:
            raise Exception(f"unexpected drag mode: {mode}")

        coor2 = self.pixel_to_coor((e.x, e.y))
        pos2 = self.coor_to_hex(coor2)
        tactic = self.get_drag_tactic(pos1, pos2)
        if tactic is not None: coor2 = self.hex_to_coor(pos2)
        self.drag = "drag", (pos1, coor2, tactic)
        self.darea.queue_draw()

    def update(self):
        self.drag = None
        self.darea.queue_draw()

    def left_click(self, pos):
        cur = self.env.cur
        if cur.empty_mask[pos]:
            self.env.make_red_move(pos)
            self.auto_close()
        elif cur.down_mask[pos] or cur.up_mask[pos]:
            change_direction = (
                self.env.stack and
                isinstance(self.env.stack[-1], BuildSplit) and
                self.env.stack[-1].phase == 0 and
                self.env.stack[-1].pos == pos
            )
            if change_direction:
                first_connect_up = self.env.stack[-1].first_connect_up
                self.env.pop_stack()
                self.env.split_node(pos, not first_connect_up)
                self.auto_close()
        else:
            split_node = (
                self.env.waiting_for_thm and
                cur.pos_to_node[pos] not in (cur.up_node, cur.down_node)
            )
            if split_node:
                self.env.split_node(pos, self.default_connect_up)
                self.auto_close()

    def right_click(self, pos):
        if self.diagram.empty_mask[pos]:
            if isinstance(self.env.last, BuildCases):
                if self.env.last._cur_red is None:
                    node = self.env.last.main.pos_to_node[pos]
                    if self.env.last._remaining_blue is not None:
                        if node not in self.env.last._remaining_blue:
                            return
            self.env.make_blue_move(pos)
            self.auto_close()

    def on_key_press(self,w,e):

        keyval = e.keyval
        keyval_name = Gdk.keyval_name(keyval)
        # print(keyval_name)
        if keyval_name == 'Escape':
            Gtk.main_quit()
        if keyval_name == 'F2':
            self.save_steps()
            self.update()
        if keyval_name == 'F3':
            self.load_steps()
            self.update()
        elif keyval_name == 'BackSpace':
            if self.env.finished:
                self.strategy_viewer.undo()
            else:
                self.env.pop_stack()
            self.update()
        elif keyval_name == "Page_Down":
            self.set_level(self.diagram_i+1)
            self.update()
        elif keyval_name == "Page_Up":
            self.set_level(self.diagram_i-1)
            self.update()
        elif keyval_name == "a":
            self.auto_close_flag = not self.auto_close_flag
            if self.auto_close_flag:
                self.auto_close()
                self.update()
            self.button_auto.set_active(self.auto_close_flag)
        elif keyval_name == "s":
            self.run_auto_once(None)
            
    def draw_hex(self, cr):
        size = 0.8 * 1/np.sqrt(3)
        coors = [
            (size*np.sin(i*np.pi/3), -size*np.cos(i*np.pi/3))
            for i in range(6)
        ]
        cr.move_to(*coors[-1])
        for coor in coors: cr.line_to(*coor)
        cr.close_path()
        cr.fill()
    def draw_border(self, cr, down):
        if not down: cr.scale(1,-1)
        size = 1/np.sqrt(3)
        coors = [
            (size*np.sin(i*np.pi/3), -size*np.cos(i*np.pi/3)+0.07)
            for i in range(-1,2)
        ]
        coors = [(coors[0][0],0)]+coors+[(coors[-1][0],0)]
        cr.move_to(*coors[-1])
        for coor in coors: cr.line_to(*coor)
        cr.close_path()
        cr.fill()        

    def draw_arrow(self, cr, down):
        if not down: cr.scale(1,-1)
        y0 = -0.05
        y1 = 0.15
        x = 0.15
        cr.move_to(0,y1)
        cr.line_to(x,y0)
        cr.line_to(-x,y0)
        cr.line_to(0,y1)
        if down: cr.set_source_rgb(1, 1, 1)
        else: cr.set_source_rgb(0, 0, 0)
        cr.close_path()
        cr.fill()
    def draw_last_move(self, cr):
        cr.set_line_width(0.05)
        cr.set_source_rgb(0, 0, 0)
        cr.arc(0, 0, 0.2, 0, 2*np.pi)
        cr.stroke()

    def hex_to_coor(self, pos):
        y,x = pos
        return x+y/2, y*(np.sqrt(3)/2)

    def draw_at_yx(self, cr, draw_method, yx, **kwargs):
        y,x = yx
        cr.save()
        cr.translate(*self.hex_to_coor(yx))
        draw_method(cr, **kwargs)
        cr.restore()

    def draw_array(self, cr, draw_method, arr, **kwargs):
        for pos in positions_true(arr):
            self.draw_at_yx(cr, draw_method, pos, **kwargs)

    def calculate_position(self, screen_width, screen_height, border = 0.1):
        min_y = np.inf
        max_y = -np.inf
        min_x = np.inf
        max_x = -np.inf
        for i,line in enumerate(self.env.main.available_mask):
            if not line.any(): continue
            min_y = min(i-2/3, min_y)
            max_y = max(i+2/3, max_y)
            [nz] = np.nonzero(line)
            min_x = min(nz[0] + (i-1)/2, min_x)
            max_x = max(nz[-1] + (i+1)/2, max_x)
            
        if not np.isfinite(min_y): return
        min_y *= np.sqrt(3)/2
        max_y *= np.sqrt(3)/2

        size_x = max_x - min_x
        size_y = max_y - min_y

        self.scale = min(screen_width / size_x, screen_height / size_y) * (1-2*border)
        shift_x = screen_width / 2 - self.scale * (min_x + size_x/2)
        shift_y = screen_height / 2 - self.scale * (min_y + size_y/2)
        self.shift = (shift_x, shift_y)

    def on_draw(self, wid, cr):

        screen_width = self.darea.get_allocated_width()
        screen_height = self.darea.get_allocated_height()

        self.calculate_position(screen_width, screen_height)

        cr.rectangle(0,0, screen_width, screen_height)
        if self.env.finished: cr.set_source_rgb(*self.solved_bg_color)
        else: cr.set_source_rgb(*self.bg_color)
        cr.fill()

        cr.save()
        cr.translate(*self.shift)
        cr.scale(self.scale, self.scale)

        if self.env.finished:
            self.draw_strategy(cr)
        else:
            self.draw_state(cr)

        cr.restore()

    def draw_red_hexes(self, cr):

        # draw hexes
        cr.set_source_rgb(*self.red_color)
        red_hexes = self.diagram.red_mask | self.diagram.up_mask | self.diagram.down_mask
        self.draw_array(cr, self.draw_hex, red_hexes)

        # draw edge
        if self.env.finished:
            available = np.array(self.strategy_viewer.available)
            for blue, red, strategy in self.strategy_viewer.stack:
                available[red] = True
        else:
            available = self.diagram.available_mask
        if self.diagram.up_edge:
            [ids] = np.nonzero(available[0])
            if ids.size: xs = range(min(ids), max(ids)+2)
            else: xs = []
            y = -1
            for x in xs:
                self.draw_at_yx(cr, self.draw_border, (y,x), down = False)
        if self.diagram.down_edge:
            [ids] = np.nonzero(available[-1])
            if ids.size: xs = range(np.min(ids)-1, np.max(ids)+1)
            else: xs = []
            y = self.diagram.height
            for x in xs:
                self.draw_at_yx(cr, self.draw_border, (y,x), down = True)

        # draw arrows
        self.draw_array(cr, self.draw_arrow, self.diagram.up_mask, down = False)
        self.draw_array(cr, self.draw_arrow, self.diagram.down_mask, down = True)


    def draw_state(self, cr):
        cr.set_line_width(0.1)
        cr.set_source_rgb(*self.red_color)
        # draw connections
        for a,b in self.diagram.extra_edges:
            cr.move_to(*self.hex_to_coor(a))
            cr.line_to(*self.hex_to_coor(b))
            cr.stroke()

        # draw light hexes
        empty_mask = np.array(self.diagram.empty_mask)
        if isinstance(self.env.last, BuildCases) and self.env.last._remaining_blue:
            cr.set_source_rgb(*self.light_color)
            for node in self.env.last._remaining_blue:
                [pos] = self.env.last.main.components[node]
                if empty_mask[pos]:
                    self.draw_at_yx(cr, self.draw_hex, pos)
                empty_mask[pos] = False
        cr.set_source_rgb(*self.empty_color)
        self.draw_array(cr, self.draw_hex, empty_mask)

        # draw blue nodes
        cr.set_source_rgb(*self.blue_color)
        for x in self.env.stack:
            if isinstance(x, BuildCases):
                if x._cur_blue is not None:
                    [pos] = x.main.components[x._cur_blue]
                    self.draw_at_yx(cr, self.draw_hex, pos)

        # draw red hexes with their decorations
        self.draw_red_hexes(cr)

        # draw last move annotation
        if isinstance(self.env.last, BuildCases):
            components = self.env.last.main.components
            if self.env.last._cur_red is not None:
                [pos] = components[self.env.last._cur_red]
            else:
                [pos] = components[self.env.last._cur_blue]
            self.draw_at_yx(cr, self.draw_last_move, pos)

        # draw dragged line
        if self.drag is not None:
            mode, data = self.drag
            if mode == "drag":
                cr.set_line_width(0.05)
                cr.set_source_rgb(0, 0, 0)
                pos1, coor2, tactic = data
                coor1 = self.hex_to_coor(pos1)
                cr.move_to(*coor1)
                cr.line_to(*coor2)
                cr.stroke()

    def draw_strategy(self, cr):

        # draw red hexes with their decorations
        self.draw_red_hexes(cr)

        # draw empty hexes
        empty = positions_true(self.strategy_viewer.available)
        for pos in empty:
            strategy_class = self.strategy_viewer.pos_to_class[pos]
            color = self.strategy_viewer.colors[strategy_class]
            cr.set_source_rgb(*color)
            self.draw_at_yx(cr, self.draw_hex, pos)

        # draw moves
        cr.set_source_rgb(*self.blue_color)
        for blue_pos, _, _ in self.strategy_viewer.stack:
            self.draw_at_yx(cr, self.draw_hex, blue_pos)
        cr.set_source_rgb(*self.red_color)
        for _, red_pos, _ in self.strategy_viewer.stack:
            self.draw_at_yx(cr, self.draw_hex, red_pos)

        # annotate last moves
        if self.strategy_viewer.stack:
            for pos in self.strategy_viewer.stack[-1][:2]:
                self.draw_at_yx(cr, self.draw_last_move, pos)

if __name__ == "__main__":

    import argparse

    cmd_parser = argparse.ArgumentParser(prog='hex_gui.py',
                                     description='interactive prover of Hex templates',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    cmd_parser.add_argument("file_name", type=str, help="file with hex diagrams, expected 'hdg' or 'json'")
    cmd_parser.add_argument("--start_level", type = int, default = None, help="the first diagram displayed at start, by default first unsolved")
    cmd_parser.add_argument("--proof_dir", type = str, default = "./proofs", help="directory storing the proof files")
    cmd_parser.add_argument("--auto", action = "store_true", help="enable automation at start")
    config = cmd_parser.parse_args()
    
    if config.file_name.endswith('.hdg'):
        suffix = '.hdg'
        diagrams = HexDiagram.parse_file(config.file_name)
        bare_fname = config.file_name[:-len('.json')]
    elif config.file_name.endswith('.json'):
        suffix = '.json'
        puzzles = HexPuzzle.parse_file(config.file_name)
        for i,puzzle in enumerate(puzzles):
            puzzle.diagram.comments.append(f"Puzzle {i+1}")
        diagrams = [
            puzzle.diagram
            for puzzle in puzzles
            if puzzle.start_red and puzzle.first_pass
        ]
    else:
        raise Exception(f"Filename must end with '.hdg' or '.json', got '{config.file_name}'")

    base_name = os.path.basename(config.file_name)
    pack_name = base_name[:len(base_name)-len(suffix)]

    win = HexGUI(
        diagrams,
        pack_name,
        start_level = config.start_level,
        proof_dir = config.proof_dir,
        auto_close_flag = config.auto,
    )
    Gtk.main()
