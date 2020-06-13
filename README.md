
# OSIRIS WEB GUI

## About: ##

* In this project, a GUI is created for the user to interact with the OSIRIS Hardware Unit. It allows the user to visualize the configuration
instead of typing it through the command line. GUI is responsible for displaying current configuration, getting user inputs and sending requests to a flask server in order to execute python scripts. REACT javascript library is used to implement the Front End. Back end is created using Flask web framework which interfaces with the existing Python scripts.

## Installation: ##
   

## Usage: ##

  ![OSIRIS WEB GUI]()
    
## How: ##
### Directory Stucture ###

- public: The public folder contains the HTML file
- src/components: React components (functional components) can be found in this file. Under each directory there are files with `jx` or `jsx` extensions. Those files contain the code for the components. The files related to styling can also be found under each directory with `.css` or `sass` extensions
- src/utils: This directory contains files with the code that performs API calls to Flask server.
- scripts: Python scripts triggered by the GUI on the Front End
- App.js: Main component in React which acts like a container for other components
- index.js: Main component loads into an html element with id `root` by reactDOM library 
- config.json: Configuration file in JSON format
- hello.py: Contains the code for the Flask Server that receives requests, executes Python scripts, read/write/updates configuration file and send responses to the client.

### Client Side Pages: ###

### Home ###

The home page will show the latency and throughput data for each subflow proxy. Home will pull data every interval (defined in OSIRIS IP Settings) 

To connect this page to a real script, please refer to `delayspeed.py` as an example. Instructions are as follows. 
- Expected input is in this format  *`getConnectionDataRefresh(subProxyIP1, subProxyIP2, subProxyIP3, subProxyIP4, delay)`*
**NOTE DELAY SPEED IS DEFINED BY THE CONFIG FILE CURRENLY AND IS ONLY USED AS A MEANS TO DETERMIND THE DATA COMING IN PER SECOND
- Expected output NEEDS to be in the manor *export = [{`subFlowLatency`:sub1Latency, `subFlowThrUp`:TX_Mbps,`subFlowThrDown`:RX_Mbps},{`subFlowLatency`:sub2Latency, `subFlowThrUp`:TX_Mbps,`subFlowThrDown`:RX_Mbps},{`subFlowLatency`:sub3Latency, `subFlowThrUp`:TX_Mbps,`subFlowThrDown`:RX_Mbps},{`subFlowLatency`:sub4Latency, `subFlowThrUp`:TX_Mbps,`subFlowThrDown`:RX_Mbps}]*


Other than this, the function that happens within is of no concern. 


### Forward Config ###

  Current ports are listed in a readonly field. User can add to or overwrite the existing ports. Either `,` seperated individual ports or `-` separated port ranges (e.g 100-200) can be entered. Port numbers can be in the range 1 to 65535. They consist of decimal numbers. When port ranges are entered first range should be smaller than second range (e.g 100-200, but not 200-100). If user enters a value conflicting those rules,  proper error messages are displayed to the user. When `new` button is clicked, the list of ports entered by the user replaces the existing ports, in case `append` is clicked the ports entered by the user will be appended to the existing ones and resulting port list will be displayed on the read-only area. Clicking `reset` button causes empty list of ports to be saved in the configuration file. To display the existing ports API GET call will be made to the route `/getForwardConfig` by the client. To overwrite, append and reset ports, API POST calls will be made to the route `/setForwardConfig`. API post call causes the `addForward.py` script to be executed. In `addForward.py` script, if user entered existing ports; those will be ignored and port ranges will be saved as individual ports in the configuration file. `addForward.py` takes 2 argument: Boolean value to indicate ports will be appended or not and list of ports.

### Modem Config ###

    This page obtains the gateway IPs by calling the API GET to route `/nconfig` from the client. Each gateway IP is shown on clickable cards which will open a new tab with the IP address and port number with `HTTP://`. API GET call is set in `components/ModemCard/index.js`. the API checks the config.json file

### Network Config ###

  In this page, existing IP configurations for 4 subflows are listed by making  API GET calls to the route `/nconfig` from the client. Subflows can be enabled or disabled and Connection Name, Gateway IP address, IP address and proxy IP address fields can be updated. When `apply` button is clicked, the updates will be written to the configuration file  by making API POST call  to the address `/nconfig`. In the `config.json` file, the list of IP configuration objects can be found assigned to `wan` property. When `reset` button is clicked, all the fields in the sections which are not disabled are reset so user can enter new values directly. Each IP address is checked if it's valid according to IPV4 when user fills IP fields. Apply button is disabled if there are any error messages. When all fields are valid, apply button is enabled again.

### Mode ###

    This page will obtain three statuses: HAIPE status, the client status, and the server status, all from `config.json` using the API GET request. API is called in `components/Mode/index.js`. Once the apply button is clicked, the page will call a POST request to update `config.json`

### User Settings ###

The purpose of this page is to give the client the ability to change their username and password. After the user has signed in, all they must do to change their username or password is to type in their desired new username and/or password in the delegated `input` fields respectively and click `submit`. From this point on, the client must use this new username and password to sign in to use the application.

### OSIRIS IP ###

The purpose of this page is to give the client access to be able to change the desired Osiris IP address and data refresh rate. Change the Osiris IP or data refresh rate in the given `input` fields by typing in the new information and pressing `submit` for either/both respective `input` fields. From this point on the application will read and use this new information.
 

## Credits: ## 
Aysen Unlu - @LinkedIn: https://www.linkedin.com/in/aysenunlu/
Jonathyn Major @LinkedIn: https://www.linkedin.com/in/jonathyn-lee-84445a7b/
Kingsley Ramos @LinkedIn: https://www.linkedin.com/in/kingsleyramos/
Ryan Mosley @LinkedIn: https://www.linkedin.com/in/ryan-mosely-a85609189/

## Licence: ##
SOLE PROPERTY OF MIMYR, OFFICAL USE OUTSIDE OF THIS ORGANIZATION IS SUBJECT TO LEGAL ACTION
