
<!-- ABOUT THE PROJECT -->
## About

A simple CLI tool for checking the current status of [Logz.io](https://logz.io) components per region.

### Built With

* [Python 3](https://www.python.org/)
* The following packeges (see [requirements.txt](https://raw.githubusercontent.com/boofinka/logzio-status-public-cli/main/CLI/requirements.txt)):
   * os
   * sys
   * requests
   * json


### Step-by-step Instructions

1. Clone the repo
   ```sh
   git clone https://github.com/boofinka/logzio-status-public-cli
   ```

2. Navigate to the CLI folder

3. install required packages:
   ```sh
   pip3 install requirements.txt
   ```

4. Run the script:
   ```sh
   python3 statusPageAPI.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

### Integration

If you wish to integrate the tool into your existing code instead of using it as a CLI, I've included [a version of the code](https://raw.githubusercontent.com/boofinka/logzio-status-public-cli/main/CLI/integrationCode.py) that ommits the menu; use the `region_dict` to select the region you wish to check.

<p align="right">(<a href="#top">back to top</a>)</p>
