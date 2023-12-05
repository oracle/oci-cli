# o - a smart oci-cli wrapper
<!-- Project o - helper smart wrapper oci cli user experience -->

**`o`** helps you use the Oracle Cloud Infrastructure's `oci` command line interface.  With **`o`** you can
 - quickly find a command and get usage info
 - simply run commands using *resource names*, not OCIDs
 - easily get the output you want

**`o`** uses shortcuts for *everything*.  All commands, parameters, and resource names have intuitive, *automatic* shortcuts.
You can run most commands with no scripting. Say goodbye to saving OCIDs to variables.

**``o``** instantly transforms this:
```
$ o list subn -c sales -v west -a
```
into this ready-to-run ``oci`` command:
```
$ oci network subnet list \
   --compartment-id ocid1.compartment.oc1..aaaaaaaaid7ybnzph4hmx46tohdg6cnclyc343hkevcosxwcsmycxamcujfa \
   --vcn-id ocid1.vcn.oc1.iad.aaaaaaaaxlfwxbld5nvhzgkot7p5dj52qv52lesn3kevcocemubg5uy6pj5q
   --all
```
**``o``** works similar magic with output.  Where ``oci``'s JSON output is suitable for computers, **`o`** output is designed for humans:
```
$ o -o name#shape#shape-conf.ocpus#state list comp inst -c kevco.

display-name shape               ocpus lifecycle-state
atos         VM.Standard.E4.Flex 1.0   STOPPED
cron         VM.Standard.A1.Flex 1.0   RUNNING
zara         VM.Standard2.4      4.0   RUNNING
humans       VM.Standard2.1      1.0   STOPPED
robotics     VM.Standard.E2.1    1.0   RUNNING
```
**``o``** picks just what you want from the output.

<a name="install"></a>
## Installation

**Important:** `oci` must *installed* and *configured* in order to use `o`.  `o` does not replace `oci`, but helps you *use* `oci`.

### Linux, CloudShell, Mac
To install, get **`o`** from github, make it executable, and place it in your PATH (perhaps in the same place as ``oci``).<br>
Paste these commands into your bash shell to download `o` and install it in your `~/bin` or next to `oci`.
```
src=https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/examples/project_o && curl -so o $src/o && chmod +x o && curl -so $HOME/.oci/oci_commands $src/oci_commands
[ -d $HOME/bin ] && ( mv o $HOME/bin && printf "\no installed in $HOME/bin/o\n" ) || ( where=$(which oci) && to=${where%ci} && [ -w $to ] && ( mv o $to && printf "\no installed in $to\n" ) || printf "\n$to: not writable\nTry:\n    sudo mv o $to\nor\n    mkdir $HOME/bin && mv o $HOME/bin\n" )
```

#### CloudShell Note
If you do not have a `$HOME/bin`, `o` will be installed in a location that is overwritten when CloudShell is updated. If this happens, it's easy to reinstall.<br>
Or you can install `o` into your ``$HOME/bin``, which is preserved during CloudShell updates.  First:
```
mkdir -p $HOME/bin $HOME/.oci
echo 'PATH=$HOME/bin:$PATH' >> $HOME/.bashrc
```
Then run (or re-run) the Linux installation commands.

### Windows
**`o`** version 1.6 was tested and runs in Windows PowerShell or Command shell, but installation not automated. **`o`** is not tested on Windows with each release, so please report an issue if it stops working.

Use this curl command to get **`o`**.  Then copy it to somewhere in your PATH.
```
curl -so o.py https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/examples/project_o/o
```
Update your PATHEXT to make it execute as `o` instead of `o.py`.

### Setup

When you first run `o` it will tell you run `o oci_commands` to create the commands file *$HOME/.oci/oci_commands*.  This collects a list of all possible `oci` commands with usage details.  This should take about two minutes.  If it doesn't work (in Windows) or runs slowly (python 3.6), copy `oci_commands` from another source to *$HOME/.oci/oci_commands*.

Then `o` asks you to run `o <tenancy_ocid>` to initialize your *$HOME/.oci/ocids*.  This seeds your *ocids* file with OCIDs of the compartments in your tenancy.  If this doesn't work it probably means that your `oci` is not configured properly.

#### Updates and maintenance

Check this page for updates...  See [New in version](#newinversion) sections below, and compare the latest with the version shown in `o help`.

To install an `o` update, just re-run the two-line [installation command](#install) above.

Update `oci` every few months (or more frequently to keep up with the latest service additions).  See [Upgrading the CLI](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliupgrading.htm).

After you update `oci`, also update *$HOME/.oci/oci_commands* with the latest commands and services:
 - `rm $HOME/.oci/oci_commands`
 - `o oci_commands`

Keep using your existing *$HOME/.oci/ocids* file.  If, however, it becomes unusable (with old data) or you want a fresh start, simply remove it and create a new one:
 - `rm $HOME/.oci/ocids`
 - `o <tenancy_ocid>`

This will get a fresh list of all compartments in the tenancy, which is a great starting point.

## Things you can do with ``o``

 - find the desired `oci` command from thousands of possible commands
 - use shortcuts to commands - the *service*, *resource* or *command* can appear in any order - or may even be omitted
 - get REQUIRED PARAMETERS and OPTIONAL PARAMETERS
   - *instantly* get usage help as you search for the command
   - *concise* usage typically fits on one screen - no scrolling or searching for the parameter you want
 - expand parameter shortcuts into full parameter names
   - use the first letter of each word for any multi-word parameter, e.g. ``-wfs`` expands to <nobr>``--wait-for-state``</nobr>
 - accept *resource name* in place of OCID values
 - resolve ambiguous *resource name*s
   - resources can be identified by *compartment/name*
   - finds match for partial entry of *name*, *display-name*, *compartment*/*name*
   - identical names can be resolved by using a substring from the OCID
     - for example, ``-c ujfa`` would specify the *sales* compartment. The last four to six characters will uniquely identify most resources.
     - handy when your resource names contain spaces or special characters
 - support ``--*-ids`` parameters where a list of OCIDs is expected, e.g. ``--security-list-ids``
   - comma-separated list of resource names is converted to a JSON list of OCIDs
 - simplify [datetime] parameters
   - ``--start-time today`` beginning (midnight) of current day (UTC)
   - ``--start-time today-36h`` - the day before yesterday at Noon
   - ``--end-time now`` - current day+time (UTC)
 - output in *table, text, csv* or *JSON* format. Format is based on your field separator
    - *table:* `-o display#lifecycle` or `-o 'display|lifecycle'`
    - *text:* `-o display/lifecycle` - displays one field per line
    - *csv:*  `-o display,lifecycle`
    - *JSON:* `-o json` Show unfiltered JSON output from ``oci``
    - Advanced: custom (pythonic) string formatting to truncate long values<br>
      `-o 'display{:.20}|create{:10.10}|id{:>8.8}'` will show a table of:
      - the first 20 characters of *display-name*  The column with be sized to fit the longest name, up to a maximum of 20 characters.
      - the first 10 characters of *time-created*  The column will be exactly 10 characters
      - the last 8 characters of *id* (the OCID)
 - output field selection is easy (no JMESpath or jq needed!)
   - easy-to-read default output useful in many cases
   - a *partial field name* can match multiple fields.
     - `-o name#domain` selects *display-name* plus *availability-domain* and *fault-domain*
   - exact field name selects matching field, but not others that partially match.
     - *id* in `-o name#id` selects the id (OCID of *this* resource) but not *image-id* or other ids in the same record
 - quick lookup of full OCIDs from *resource name* or partial OCID
    - `o ocids compartment` *instantly* shows the full OCIDs for all compartments
    - `o ocid  sales/bastion` *instantly* shows the full OCIDs for the specified compartment

#### New in version 1.3 (2022-12-15)
 - Get next page of results with `o <repeat-last-command> -page next`
 - Select child fields from complex output with `-o key.subkey`
   - first use `o -o / <command> .` to see all available keys, then rerun with desired output list
   - Example:  `o -o +shape-conf.ocpus#shape-conf.memory` list compute inst -c sales .`
 - Take JSON input from file. Useful for getting the format just right
   - First save `oci` output (or output from `o -o json`) to a file
     - `o -o json list compute instances > list.json`
   - Then use that as input to `o`
     - `o -i list.json -o name:20#id:-.10#created:.10`

#### New in version 1.4 (2023-01-20)
 - Assist with compartment names with OCIDs in some searches:
   - `o structured-search --query-text 'query instance resources where compart=sales'`
   - `o logging-search -sq 'search sales' -ts yesterday -te today`
 - Easier custom output formatting:
  - braces are optional
  - allow ":-" instead of ":>" for right-justify (so quotes aren't needed around the ">")
   - Example:  For table output with right-most 8 characters of `id`, 10 (or more) characters of `display-name`, and first 10 characters (no more than 10) of `time-created`
    - `o -o id:-.8#name:10#create:.10 comp inst list`

#### New in version 1.5 (2023-02-27)
 - If you like the default output but want to add another field use `-o +field`:
   - Example: `o -o +subnet list-vnics -c sales`
 - If you like the default output fields, but want to change the format style, just add the separator:
      - change to "text" output: `o -o +/ <command>`
      - change to CSV output: `o -o +, <command>`
      - change to "text" and add fields: `-o +/subnet list-vnics ...`
 - Show additional output fields (not in "data") to stderr, such as "etag" or os "prefixes".  Use `o -q` to hide this non-data.

<a name="newinversion"></a>
#### New in version 1.6 (2023-04-03)
 - **o** runs on *Windows* PowerShell and Command shell. Not fully tested, but the basics appear to work.
   - Download `o` and put it in your PATH:
 ```
 curl -o o.py https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/examples/project_o/o
 ```
   PATHEXT should contain `.PY` to allow execution of `o.py`
   - oci_commands generation doesn’t work, so pull the file from another system and copy it to your `.oci\oci_commands`
 - Output from the last command is saved to `.oci/.otmp` if `.oci/.otmp` exists
   - re-format the output by running `o -o <format>` with no oci command or parameters
   - `o -o/` is useful for seeing what fields are available in the data
   - `o -oj` shows JSON output
   - `o -o name#id:.10#...` - customize the format without needing to rerun the `oci` command
   - to activate this feature, simply touch `$HOME/.oci/.otmp`
 - Added “reg" column to identify region key in default table output
   - This is not shown nor available in csv or text formats.
   - Region isn't in the resource data for most data types. **o** is extracting it from the ocid
 - **o** runs on *Windows* PowerShell and Command shell. Not fully tested, but the basics appear to work.

#### New in version 1.9 (2023-07-05)
- "Best match" command selection adjusted to accept shorter input for commands in common, core services.  This was needed because oci-cli supports more services and more commands than before, making it more difficult to find unambiguous shortcuts.
- More shortcuts for `o structured-search --query-text` where clauses:
   - Use `c` or `l` for "compartment" or "lifeCycleState", followed by `=` or `!=` and the name of a compartment or lifeCycleState.  Don't worry about quotation marks around terms. E.g.
      - `query all resources where (c = sales || c = kevco) && l != terminated`

#### New in version 1.10 (2023-08-08)
- Improved selection of availability domain for users with multiple regions and tenancies. `-ad 1` will choose the right AD for the active tenancy and region.
- `o` can work with identity-domains.<br>
  First, `o iam domain list` to list your identity-domains.<br>
  Then
  - Get a list of users: `o id list users -end <domain-name>.`
  - Get a list of groups: `o id list groups -end <domain-name>.`
  - Get a list of users with group memberships of each user:<br>
  `o -o display/user-name/groups.display id user list --attributes displayName,name,groups -end <domain-name>.`
  - Get a list of groups with user members for each group:<br>
  `o -o display-name/member.name id list groups --attributes name,members -end <domain-name>.`

#### New in version 1.11 (2023-11-22)
- Improved handling of very long results (especially `o os list objects --all`)
- Minor bugfixes

## How **``o``** works  
 - **``o``** compares your input with thousands of ``oci`` commands, and uses an fuzzy matching to find the command you want.

 - **``o <command>``** provides a usage synopsis, showing required and optional parameters for matching commands.  Add "help" to the end to see global parameters as well.  E.g. <nobr>``o <command> help``</nobr> provides the usage synopsis with global parameters, while <nobr>``o <command> --help go``</nobr> runs <nobr>``oci <command> --help``</nobr>.

 - You add option and parameter shortcuts, and **``o``** shows you the complete ``oci`` command line after performing command, option, and parameter expansions and substitutions.

 - Options for **`o`** such as `-o field#list` must appear *before* the `<command>`  specification. `oci` options must appear *after* `<command>`.  While this ordering is not strictly required by `oci`, `o` uses this to determine which options are for `o` and which are for `oci`.

 - Add `go` or `.` to the end of the command and **``o``** will execute the ``oci`` command.  Add `!` to force run (sometimes needed when `o` doesn't know the command is complete).

 - ``oci`` returns JSON data when you create, get, list, or update resources.  **``o``** captures resource names and Oracle Cloud IDs (OCIDs) and saves these to your *$HOME/.oci/ocids* file. **``o``** later uses this information to find resources by name, and to translate names to IDs.

 - **``o``** scans the JSON data from ``oci`` for key names that match or partially match any of your <nobr>``-o key/word/list``</nobr>.  The key words determine *what* presented, while the **``/``** separator character determines *how* they are presented.

##  <a name="requirements"></a> Requirements

You will need:

- ``oci`` - The Oracle Cloud Infrastructure command line interface must be *installed and configured*.
  - Try running ``oci os ns get`` to verify that it's authenticating okay.
  - See https://docs.cloud.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm
  - You need sufficient permissions in your tenancy
    - **Authorization failed or requested resource not found** often means you connected to the cloud okay, but policies don't allow you to do what you tried to do.
    - Minimally you need permission to **inspect** resources in order for most commands to work.
- ``oci`` must be in your PATH so that ``o`` can find it
- Python 3.6+.  If ``oci`` is installed, you have Python.  (`oci` and `o` work better with python 3.7+)

**OCIDs File**

**``o``** uses a local cache of OCID-to-name mappings called the OCIDs file, located at *$HOME/.oci/ocids*.  This is populated during setup when you run `o <tenancy_ocid>`.  

To use **``o``** with additional tenancies, simply set your OCI_CLI_PROFILE and run `o <tenancy_ocid>` with the new tenancy OCID.

As resources are deleted from your tenancy, **``o``** does automatically remove these from the OCIDs file.  Also, as other tenancy users make changes in the tenancy, these changes won't be reflected in your OCIDs file.  When these stale OCIDs cause problems with ``o``'s name matching, they may be removed from the OCIDs file with ``o prune <resource-name>``.  Or you can start with a fresh OCIDs file by removing  *$HOME/.oci/ocids* and run `o <tenancy_ocid>`.

**oci_commands File**

When you run `o oci_commands`, `o` takes a minute or two to build a list of the thousands of possible `oci` commands with their options, and saves this to *$HOME/.oci/oci_commands*.  This list is generated on your system to ensure that it matches the commands in your installed version of `oci`.

In some cases (in Oracle provided OS images) the `oci` command line environment come be pre-installed, but with incomplete documentation.  If so, `o` may take an hour or more to gather the command information.  To avoid this you can: copy an *oci_commands* file from another source (preferably with a similar `oci` version) to *$HOME/.oci/oci_commands*; or reinstall oci-cli to ensure the full documentation is included.

`oci_commands` should be rebuilt after updating or reinstalling oci-cli.  To do this:
 - remove the old file:  `rm $HOME/.oci/oci_commands`
 - Rebuild with: `oci oci_commands`

**Advanced Setup and Usage**

If you use ``oci`` with *instance_principal* authentication, set `` OCI_CLI_AUTH=instance_principal`` in your environment
(rather than use <nobr>``--auth instance_principal``</nobr> with each command).

If you have multiple profiles in your *.oci/config* file, set OCI_CLI_PROFILE for the desired profile before running ``o <tenancy_ocid>`` to set up your *.oci/ocids* file for that profile, or before running other ``o`` commands.

Use [CLI Environment Variables](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/clienvironmentvariables.htm) to ensure these settings are passed on to the ``oci`` commands run by ``o``.  This is especially important during tenancy setup, when **``o``** executes four ``oci`` commands to seed the *.oci/ocids* file, but you may find environment variables more convenient than adding extra parameters to each command.

If you use ``oci`` for multiple tenancies, by default ``o`` will save OCIDs for all tenancies in the same *$HOME/.oci/ocids* file.  However, if you want to keep the OCIDs separated, ``o`` will first look in the current working directory for *./ocids* before looking for *$HOME/.oci/ocids*.  The file is always initially created in *.oci/ocids*, but you can copy this to a tenancy specific directory.  Then when you run ``o`` while in that directory it will use the tenancy specific *ocids* file.  Remember to secure your *ocids* files with permissions set to 0600.

## Supported platforms

**``o``** works on MacOS and Linux (including Windows WSL) and Oracle CloudShell.

**``o``** version 1.6 introduces partial support for Windows PowerShell and Command shell.  The `o` command works, but installation and setup are not automated.

## Design principle

Keep it simple.  

 - **``o``** does not have a configuration file
 - **``o``** does not use environment variables (``oci`` does)
 - **``o``** minimizes typing (thus its one-letter name)
 - **``o``** is forgiving
   - accepts plurals when singular is expected
   - accepts ``-`` when ``--`` is expected
   - accepts command words in any order
   - deals with missing words (e.g. no *service* name)
 - **``o``** is fully implemented in one source file (for as long as practical)
 - **``o``** is fast.  This lets you build commands iteratively, one parameter at a time, before executing them.

New features should not burden **``o``**'s basic functionality with user complexity.

### Author

**``o``** was conceived and written by Kevin Colwell in 2020.
