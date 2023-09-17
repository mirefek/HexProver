import logic_core as core

def get_types(rule, numargs):
    if rule == core.build_case_strategy:
        assert numargs > 0 and numargs % 2 == 0
        return [int, core.Proof]*(numargs // 2)
    elif rule == final_pack:
        return [core.Proof]*numargs
    else:
        varnames = rule.__code__.co_varnames
        varnames = varnames[:rule.__code__.co_argcount]
        annot = rule.__annotations__
        res = [annot[varname] for varname in varnames]
        # rename theorems to proofs
        res = [core.Proof if x == core.Theorem else x for x in res]
        return res

def export_proof_arg(x, proven):
    if isinstance(x, (int, core.Clause, core.Atom)): return str(x)
    elif isinstance(x, dict):
        items = sorted(x.items())
        src, target = zip(*items)
        assert all(isinstance(a, int) for a in src), [type(x) for x in src]
        assert all(isinstance(a, int) for a in target), [type(x) for x in target]
        src = ' '.join(map(str, src))
        target = ' '.join(map(str, target))
        return src+" -> "+target
    elif isinstance(x, frozenset):
        assert all(isinstance(a, int) for a in x)
        return ' '.join(map(str, sorted(x)))
    elif isinstance(x, core.Proof): return proven[x]

def parse_proof_dict(s):
    src, target = s.split('->')
    src = (int(n) for n in src.split())
    target = (int(n) for n in target.split())
    return dict(zip(src, target))
def parse_proof_frozenset(s):
    return frozenset(int(n) for n in s.split())

parse_proof_element_d = {
    int : int,
    dict : parse_proof_dict,
    frozenset : parse_proof_frozenset,
    core.Clause : core.Clause.parse,
    core.Atom : core.Atom.parse,
}
def parse_proof_arg(t, el, proven):
    if t == core.Proof:
        return proven[el]
    else:
        return parse_proof_element_d[t](el)

def export_proof_step(proof, proven):
    types = get_types(proof.rule, len(proof.args))
    if not all(isinstance(arg, t) for t,arg in zip(types, proof.args)):
        print(proof.rule)
        print("expected types:", types)
        print("real types:", [type(arg) for arg in proof.args])
        raise Exception("Incorrect types in a proof")
    args = [export_proof_arg(arg, proven) for arg in proof.args]
    return ' ; '.join([proof.rule.__name__]+args)
def load_proof_step(line, proven):
    rule, *args = line.split(' ; ')
    if rule == "final_pack": rule = final_pack
    else: rule = getattr(core, rule)
    types = get_types(rule, len(args))
    args = tuple(parse_proof_arg(t, arg, proven) for t,arg in zip(types, args))
    return rule(*args)

def name_generator():
    yield "theorem"
    i = 0
    while True:
        yield f"lemma{i}"
        i += 1

def export_proof(proof, stream, name_iterator = None, proven = None): # proven : Proof -> name
    if proven is None: proven = dict()
    if name_iterator is None: name_iterator = name_generator()
    if proof in proven: return

    name = next(name_iterator)
    for arg in proof.args:
        if isinstance(arg, core.Proof) and arg not in proven:
            export_proof(arg, stream, name_iterator, proven)
    step_str = export_proof_step(proof, proven)
    proven[proof] = name
    print(f"{name} = {step_str}", file = stream)

def load_proof(stream, proven = None): # proven : name -> Proof
    if proven is None: proven = dict()
    for line in stream:
        if line.endswith('\n'): line = line[:-1]
        name, body = line.split(' = ', 1)
        proven[name] = load_proof_step(body, proven)
    return proven["theorem"]

def final_pack(*args):
    return args

def export_proof_to_file(thm, fname):
    if isinstance(thm, core.Theorem): proof = thm.proof
    elif isinstance(thm, core.Proof): proof = thm
    elif isinstance(thm, (list, tuple)):
        proofs = []
        for lemma in thm:
            if isinstance(lemma, core.Theorem):
                proofs.append(lemma.proof)
            else:
                proofs.append(lemma)
        proof = core.Proof(final_pack, proofs)
    with open(fname, 'w') as f:
        export_proof(proof, f)
def load_proof_from_file(fname):
    with open(fname) as f:
        return load_proof(f)

if __name__ == "__main__":
    thm = load_proof_from_file("example.hpf")
    print(thm)
