load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "b1e80761a8a8243d03ebca8845e9cc1ba6c82ce7c5179ce2b295cd36f7e394bf",
    urls = ["https://github.com/bazelbuild/rules_docker/releases/download/v0.25.0/rules_docker-v0.25.0.tar.gz"],
)

load(
    "@io_bazel_rules_docker//repositories:repositories.bzl",
    "repositories",
)

repositories()

## SEMATIC RULES

load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

git_repository(
    name = "rules_sematic",
    branch = "main",
    remote = "https://github.com/sematic-ai/sematic.git",
    strip_prefix = "bazel",
)

load("@rules_sematic//:pipeline.bzl", "base_images")

base_images()

load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
    name = "my_python_deps",
    requirements = "//third_party:requirements.txt",
)