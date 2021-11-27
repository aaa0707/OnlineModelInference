# Model Inferencing on Server

This Repo contains code for running inference based on two models whose inputs are Amino Acid sequences of lengths 50

##### Logic of inferencing

model1 and model2 both return float values. We want to return a list of amino acid sequences where model2 returned a value > 0. Additionally, we want to take the top 100 elements according to model1 scores in this filtered list.
This returns a sorted list of Amino acids according to model1 results


##### Webapp
Additionally, this code also sets up flask app to call the models through a REST API. The flask_app.py code handles the requests. I have also provided a docker file that can be used to setup a container and initialize the the container on a VM

