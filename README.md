# Create React App Automation
Running a script which using create-react-app to init a new project, install packages and automate project structuring


# How to Use
Requirements: Python and Node must already be installed.  

Open terminal and run the script: `python main.py react_project_name`  
Instead of 'react_project_name' enter you react project name that you wish for.  
If you run the command without a project's name it will automatically assign "react_project"

# How it works
1. Creating React Application via create-react-app. (https://github.com/facebook/create-react-app)
2. Structuring the Project which is described in `folders.json` file:
```
components
containers
assets/images/
hoc
store/actions
store/reducers
```
3. Installing Packages which is described in `packages.json` file:
```
react-router
react-router-dom
redux
react-redux
redux-thunk
```

