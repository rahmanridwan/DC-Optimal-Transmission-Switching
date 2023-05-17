# DC-Optimal-Transmission-Switching

For this project, we are using the IEEE 118 bus system to generate data and predict outputs with transmission switching on specific transmission lines. 

The generated data consist of:
Scenario: The different scenarios where different numbers of switchings take place
SwitchNum: The number of switching for specific scenarios
Pd1-Pd118: load vector
Pg1-Pg18: generation vector
Theta1-Theta118: voltage phase angle
Flow1-Flow186: flow vector
z1-z186: The output. Each transmission line shows whether switching takes place in the boolean format
cost: the cost of switching for specific scenarios
SwitchId: on which transmission line the switching takes place for a given SwitchNum and Scenario

We create a Neural Network model and train the dataset with the load vector as the input variable, and the z1-z186 as the target variable. Then we try to predict the output with a high accuracy.

The project also includes congestion data, where:
Filename: congestion_data_4_19.csv

 

Description: Generated data describing congestion and the associated optimal switching action(s).

Columns:

Scenario & SwitchNum, exactly the same as other data
Pd1 – Pd118, also the same as before
LMP1 – LMP118: the locational marginal price associated with each bus. Recall that this is the dual variable associated with the node balance constraint. It, therefore, describes the change in objective value associated with a unit increase in demand at that bus. Large values suggest congestion.
Dg1 – Dg19: the dual variable associated with the maximum capacity of each generator. This describes the change in objective function associated with a unit increase in capacity for a given generator. Negative values suggest congestion.
Bc1 – Bc186: Branch capacity. This is simply the maximum flow for a branch minus the absolute value of the flow (since it can flow in either direction). 0 describes a fully-loaded line, and hence congestion.
Z1 – z186: the switch status of each line for a given scenario & switchnum. Note that this is coded slightly differently than our other data. Here we only mark the precise switch we are interested in, rather than all open switches.
Cost & switchId: exactly the same as other data.

Due to the large size of the datasets, they could not be uploaded on the github repository. However, the link to the shared onedrive is provided for access to the datasets. 
https://texastechuniversity-my.sharepoint.com/personal/eric_brown_ttu_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Feric%5Fbrown%5Fttu%5Fedu%2FDocuments%2FResearch%2FProjects%2FTransmissionSwitching%2FRidwan%2Fshared%20folder&FolderCTID=0x0120004C9CC705AC35334897493FBA3C62C0DF&view=0
