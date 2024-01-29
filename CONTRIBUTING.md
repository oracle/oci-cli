# Contributing to this repository

We welcome your contributions! There are multiple ways to contribute, even if
you're not a developer.

## Opening issues

If you think you've found a security vulnerability, do not open a GitHub issue.
Instead, follow the instructions in our [security policy](./SECURITY.md).

To report a bug or request an enhancement that is not related to a security
vulnerabiliity, open a GitHub issue. When filing a bug, remember that the better
written the bug is, the more easier and more likely it is to be reproduced and
fixed.

## Pre-requisites for code or documentation submissions

Before we can review or accept any source code or documentation-related
contribution, you will need to digitally sign the [Oracle Contributor Agreement][OCA]
(OCA) using the OCA Signing Service. This only needs to be done once, so if
you've signed it for another repo or project, there is no need to sign again.

All your commit messages must include the following line using the same name and
email address you used to sign the OCA:

```text
Signed-off-by: Your Name <you@example.org>
```

This can be automatically added to pull requests by committing with `--sign-off`
or `-s`, e.g.

```text
git commit --signoff
```

We can only accept pull requests from contributors who have been verified as
having signed the OCA.

## Pull request process

1. Ensure there is an issue created to track and discuss the fix or enhancement
   you intend to submit.
1. Fork this repository
1. Create a branch in your fork to implement the changes. We recommend using
   the issue number as part of your branch name, e.g. `1234-fixes`
1. Ensure that any documentation is updated with the changes that are required
   by your change.
1. Ensure that any samples are updated if the base image has been changed.
1. Submit the pull request. *Do not leave the pull request blank*. Explain exactly
   what your changes are meant to do and provide simple steps on how to validate
   your changes. Ensure that you reference the issue you created as well.
1. We will assign the pull request to specific people for review before it is merged.

## Code of conduct

Our [Code of Conduct](./CODE_OF_CONDUCT.md) is adapted from the
[Contributor Covenant][CC], version 1.4, available at
 <https://www.contributor-covenant.org/version/1/4/code-of-conduct.html>.

[OCA]: https://oca.opensource.oracle.com
[CC]: https://www.contributor-covenant.org
