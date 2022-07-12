# o - a smart oci-cli wrapper
**`O`** accelerates your use the Oracle Cloud Infrastructure's `oci` command line interface.  With **`o`** you can
 - quickly find the right command
 - get concise usage help
 - build the `oci` command using *resource names*, not OCIDs
 - get easy-to-read output in multiple formats
 - use shortcuts for *all* commands, parameters, resource names - no need to predefine aliases!

With **`o`**  you can run most ``oci`` commands with no scripting. You no longer have to save OCIDs to variables in order to build a command.

Through clever substitution, **``o``** instantly transforms this
```
$ o list subn -c sales -v west -a
```
into this ready-to-run ``oci`` command
```
$ oci network subnet list \
   --compartment-id ocid1.compartment.oc1..aaaaaaaaid7ybnzph4hmx46tohdg6cnclyc343hkevcosxwcsmycxamcujfa \
   --vcn-id ocid1.vcn.oc1.iad.aaaaaaaaxlfwxbld5nvhzgkot7p5dj52qv52lesn3kevcocemubg5uy6pj5q
   --all
```
**``o``** works similar magic on output.  Where ``oci``'s JSON output often spews hundreds of lines like this
```
{
  "data": [
    {
      "availability-domain": "VLKn:US-ASHBURN-AD-3",
      "cidr-block": "10.0.2.0/24",
      "compartment-id": "ocid1.compartment.oc1..aaaaaaaaid7ybnzph4hmx46tohdg6cnclyc343kevcossxwcsmycxamcujfa",
      "defined-tags": {},
      "dhcp-options-id": "ocid1.dhcpoptions.oc1.iad.aaaaaaaar7wdbqmpxs4d7aj3lih7bs2a5bwkevco7ngxbmr7thwzcntpw6ta",
      "display-name": "Public Subnet VLKn:US-ASHBURN-AD-3",
      "dns-label": "sub01281626512",
      "freeform-tags": {},
      "id": "ocid1.subnet.oc1.iad.aaaaaaaadomh23d27sli42hhrb2jo3hzock2l5u4kevconnlpdt5h2ocwn7a",
      "lifecycle-state": "AVAILABLE",
...
```
with **``o``** you get this
```
$ o -o display#life#cidr-block#compartment list subn -c sales -v west go

display-name                       lifecycle cidr-block  compartment-id
Public Subnet VLKn:US-ASHBURN-AD-3 AVAILABLE 10.0.2.0/24 sales
Public Subnet VLKn:US-ASHBURN-AD-2 AVAILABLE 10.0.1.0/24 sales
Public Subnet VLKn:US-ASHBURN-AD-1 AVAILABLE 10.0.0.0/24 sales
```
**``o``** default output is a table of commonly useful fields, but **``o``** makes it easy to pick just what you want (as seen in the above example).

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
 - support [complex type] parameters where a list of OCIDs is expected
   - comma-separated resource names are converted to a JSON list
 - simplify [datetime] parameters
   - ``--start-time **today**`` beginning (midnight) of current day (UTC)
   - ``--start-time **today-36h**`` - the day before yesterday at Noon
   - ``--end-time **now**`` - current day+time (UTC)
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
    - `o ocid  sales/bastion` *instantly* shows the full OCIDs for all compartments

## How **``o``** works  
 - **``o``** compares your input with thousands of ``oci`` commands, and uses an intelligent algorithm to find the best match.

 - **``o <command>``** provides a usage synopsis, showing required and optional parameters for matching commands.  Add "help" to the end to see global parameters as well.  E.g. <nobr>``o <command> help``</nobr> provides the usage synopsis with global parameters, while <nobr>``o <command> --help go``</nobr> runs <nobr>``oci <command> --help``</nobr>.

 - You add option and parameter shortcuts, and **``o``** shows you the complete ``oci`` command line after performing command, option, and parameter expansions and substitutions.

 - Options for **`o`** such as `-o field#list` must appear *before* the `<command>`  specification. `oci` options must appear *after* `<command>`.  While this ordering is not strictly required by `oci`, `o` uses this to determine which options are for `o` and which are for `oci`.

 - Add `go` or `.` to the end of the command and **``o``** will execute the ``oci`` command.

 - ``oci`` returns JSON data when you create, get, list, or update resources.  **``o``** captures resource names and Oracle Cloud IDs (OCIDs) and saves these to your *$HOME/.oci/ocids* file. **``o``** later uses this information to find resources by name, and to translate names to IDs.

 - **``o``** scans the JSON results from ``oci`` for key names that match or partially match any of your <nobr>``-o key/word/list``</nobr>.  The key words determine *what* presented, while the **``/``** separator character determines *how* they are presented.

##  Requirements

You will need:

- MacOS, Linux or WSL.
- Python 3.6+.  If ``oci`` is installed, you have Python.
- ``oci`` - The Oracle Cloud Infrastructure command line interface must be *installed and configured*.
  - Try running ``oci os ns get`` to verify that it's working.
  - See https://docs.cloud.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm
  - You need sufficient permissions in your tenancy
    - **Authorization failed or requested resource not found** often means you connected to the cloud okay, but policies don't allow you to do what you tried to do.
    - Minimally you need permission to **inspect** resources in order for most commands to work.
- ``oci`` must be in your PATH so that ``o`` can find it

## Installation

**``o``** should be in your PATH, probably in the same place as ``oci``.  Use these commands to download ``o`` from github and install it next to ``oci``.
```
o_src=https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/examples/project_o/o
where=$(which oci) && wget -q $o_src -O ${where%ci} && chmod a+x ${where%ci}
```
When you first run `o` it will tell you how to create the commands file *$HOME/.oci/oci_commands*, and then `o` helps you to initialize your *$HOME/.oci/ocids* file.

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

**``o``** should be relatively easy to port to Windows, but isn't there yet.  Volunteer?

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
