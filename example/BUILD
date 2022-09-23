load("@rules_sematic//:pipeline.bzl", "sematic_pipeline")
load(
    "@rules_python//python:defs.bzl",
    "py_library",
)
load("@my_python_deps//:requirements.bzl", "requirement")



py_library(
    name = "add",
    srcs = [
        "add.py",
        "main.py",
    ],
    deps = [
        requirement("sematic"),
    ],
)

sematic_pipeline(
    name = "main",  # the launch script of your pipeline is main.py
    registry = "558717131297.dkr.ecr.us-west-2.amazonaws.com",
    deps = [
        ":add",
    ],
)
