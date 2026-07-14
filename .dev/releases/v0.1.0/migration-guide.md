# Migration To v0.1.0

`v0.1.0` is the first historical baseline, so there is no earlier governed source version to migrate from.

For a new target repository, copy the framework and run `repo-structure-sync`. For a repository that already contains an unversioned copy, treat its exact source commit and local changes as unresolved provenance; inventory and reconcile them before claiming that the target is at `v0.1.0`.
