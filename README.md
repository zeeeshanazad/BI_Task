## EL(T) implementation

Building data pipelines and designing data models is one of the daily tasks of a data engineer.
This task requires you to implement a partial transformation of one of Homeday's data ELT pipelines, which interfaces with an external API.

### Mission Context
The data is from a partner API for Mortgage team to manage loan applications, the scheduler will request the API every hour to keep it freshness.
You can find 2 JSON files which are extracted from a single request of the API, they are both anonymized already. Each file represents an application for the loan. 

The followings are your missions requirement, please read them thoroughly before you start:
1. Apply "JSON to CSVs" transformation to those files (each JSON is a single record in the resulting CSV table) in a script.
2. Instead of resulting tables in CSV format, store them in a database system. **(Optional)**
3. Wrap the entire pipeline into a docker image. **(Optional)**
4. Use Python to construct your pipeline, save your functions or other necessary in the Python scripts (not Jupyter notebook).
5. Attach your GitHub repository or gist once you are finished. 

Feel free to reach out to us if you got any question or idea while approaching the tasks! Enjoy coding!
