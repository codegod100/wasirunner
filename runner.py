from wasmer import engine, wasi, Store, Module, ImportObject, Instance
from wasmer_compiler_cranelift import Compiler
import os


def run_module(path):
    bytes = open(path, "rb").read()
    store = Store(engine.Universal(Compiler))

    module = Module(store, bytes)
    wasi_version = wasi.get_version(module, strict=True)

    wasi_env = wasi.StateBuilder("").finalize()

    import_object = wasi_env.generate_import_object(store, wasi_version)

    instance = Instance(module, import_object)

    instance.exports._start()
