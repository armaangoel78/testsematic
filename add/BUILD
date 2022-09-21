load("@rules_sematic//:pipeline.bzl", "sematic_pipeline")
load(
    "@rules_python//python:defs.bzl",
    "py_library",
)

py_library(
    name = "add",
    srcs = [
        "add.py",
    ],
    deps = [
        requirement("sematic"),
    ],
)

sematic_pipeline(
    name = "main",  # the launch script of your pipeline is main.py
    registry = "<container-registry-uri>",
    repository = "<container-repository>",
    deps = [
        ":add",
    ],
)