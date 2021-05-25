# o - a smart oci-cli wrapper
**``O``** accelerates your use the Oracle Cloud Infrastructure's ``oci`` command line interface.  With **``o``** you can
 - quickly find the right command
 - get concise usage help
 - build the ``oci`` command using *resource names*, not OCIDs
 - get easy-to-read output in multiple formats
 - use shortcuts for *all* commands, parameters, resource names - no need to predefine aliases!

With **``o``**  you can run most ``oci`` commands with no scripting. You no longer have to save OCIDs to variables in order to build a command.

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
**``o``** shows a table of commonly useful fields by default, but makes it easy to pick and choose just what you want.

## Things you can do with ``o``

 - find the desired `oci` command from thousands of possible commands
 - use shortcuts to commands - the *service*, *resource* or *command* can appear in any order - or may even be omitted
 - get REQUIRED PARAMETERS and OPTIONAL PARAMETERS
   - *instantly* get usage help as you search for the command
   - *concise* usage typically fits on one screen - no scrolling or searching for the parameter you want
 - expand parameter shortcuts into full parameter names
 - accept *resource name* in place of OCID values
 - resolve ambiguous *resource name*s
   - resources can be identified by *compartment/name*
   - finds match for partial entry of *name*, *display-name*, *compartment*/*name*
   - identical names can be resolved by using partial OCID.
     -  For example, ``-c ujfa`` would specify the *sales* compartment in the above examples
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
    - *JSON:* `-o json` Show all attributes in unfiltered JSON
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
 - **``o``** compares your input with more than two thousand ``oci`` commands, and uses an intelligent algorithm to find the best match.

 - **``o``** then provides a usage synopsis, showing required and optional parameters.  Add "help" to the end to see global parameters as well.  End with ``--help go`` to get full ``oci <command> --help``.

 - You add option and parameter shortcuts, and **``o``** shows you the complete ``oci`` command line after performing command, option, and parameter expansions and substitutions.

 - **`o`** options such as `o -o field#list` must appear *before* the `oci` service-resource-command specification. `oci` options must appear *after*.  While this ordering may not be required with `oci`, it is needed for `o` to tell which options are for `o` and which are for `oci`.

 - Add "go" to the end of the command and **``o``** will execute the ``oci`` command.  ``oci`` typically returns JSON data when you create, get, list, or update resources.

 - **``o``** inspects the JSON results and collects selected of details about your OCI resources whenever you run any command with ``o ... go``. Most importantly, **``o``** captures resource names and Oracle Cloud IDs (OCIDs). Details are saved to your *$HOME/.oci/ocids* file. **``o``** uses this information to find resources by name, and to translate names to IDs.

 - Once **``o``** receives JSON results from oci, it scans the returned data dict for key names that match or partially match any of your ``-o key/word/list``.  The key words determine *what* presented, while the **``/``** separator character determines *how* they are presented.

##  Requirements

You will need:

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
When you first run **``o``** it will tell you how to create the commands file ``$HOME/.oci/oci_commands``, and then how to seed your ``$HOME/.oci/ocids`` file.

**Advanced setup:**  If you have multiple tenancies, or multiple profiles in your ``.oci/config`` file, setenv OCI_CLI_PROFILE for each profile as you run ``o <tenancy_ocid>`` to set up the ``$HOME/.oci/ocids`` file. This ensures that the profile is passed to the ``oci`` command on "go", and is especially important during tenancy setup, when **``o``** executes four ``oci`` commands.

## Supported platforms

**``o``** works on MacOS and Linux (including Windows WSL) and Oracle CloudShell.

**``o``** should be relatively easy to port to Windows, but isn't there yet.  Volunteer?

## Design principle

Keep it simple.  

 - **``o``** does not have a configuration file
 - **``o``** does not use environment variables
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
