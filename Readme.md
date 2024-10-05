This is the project for VAST chanllenge 2021 Mini challenge 2.

all the data files are in the folder \data, and all the data processing and visualization codes are in the folder \scripts.

# CODE FOR EACH TASK

## Task 1
The visualization tool for task 1 is \scripts\task1_vis.ipynb.

## Task 2
This task needs the result of analysis in Task 1 and the route visualization tool in \scripts\route_vis.ipynb

## Task 3
To match the credit card and loyalty card with the right card owner, we need to run \scripts\find_cardowner.ipynb

## Task 4
In Task 4 we need to analyze the the unofficial relationship. In \scripts\relationship_network_vis.ipynb we have a network graph visualization tool.

## Task 5
For Task 5, the analysis code is in \scripts\ccTransactions_analyze.ipynb.





Moreover, all the visualization based on dash can be displayed in the browser. You can find the port number in the corresponding code snippet



For example, in

``````python
if __name__ == '__main__':
    app.run_server(debug=True, port=8079)
``````

the port number is 8097, you can in the browser visit: 

```
http://localhost:8079/
```



# Environment Dependency

Our project is based on Python 3.9.6.

All the libraries you need are listed as below:

``````shell
pip install pandas
pip install datetime
pip install dash
pip install dash-cytoscape
pip install plotly
``````



