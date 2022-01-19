# Branch naming conventions
We use git branches to keep track of the versions of font sources that for each product release, and for the product currently in development. We also use temporary branches so you can work on particular features with others, without disrupting the source for the current product release.

Please use the following conventions for naming branches. Use only lowercase to keep yourself sane (and avoid merge problems).

* `master` – this is the source for the current MS product development (right now, that's RS4). The binary generated from this branch is checked into the current in-development product. This branch requires a pull request to update.

* `release/<release_name>` - this contains the sources for a past released MS product. e.g. `release/rs3` contains the source for RS3. These branches are created from master when the product releases.

* `work/<work_item>` or `work/<branch>/<work_item>` - a work / topic branch for a given work item. e.g. `work/cyrillic`, or `work/master/kern_bugfix`. Create these from `master` or a `release/` branch to do some work. It's expected that these will be destroyed after they're merged back in with their parent branch. Life is easier if these are relatively short-lived (e.g. less than a month).
