
# FastAPI to build Python Web APIs

## install fastapi and uvicorn using pip
```
 $ python -m pip install fastapi uvicorn[standard]
```

- fastapi: framework to build api
- unicorn: server that use api to serve requests

- run first api app with uvicorn
  ```
    $ uvicorn main:app --reload
  ```
- Uvicorn running on http://127.0.0.1:8000
- json response: 
```
    {"Hello":"Fast api learner"}
```
- open http://127.0.0.1:8000/docs for interactive api doc
- [Alternative] go to http://127.0.0.1:8000/redoc

#### TO DO:
- [ ] Query parameters to customize a request
- [ ] Dependency injection to handle reusable logic for permissions, database sessions, and others
- [ ] Security utilities to integrate authentication and authorization based on standards
- [ ] Background tasks for simple operations like sending an email notification
- [ ] async and await to support concurrency and improve performance
- [ ] WebSockets for advanced use cases that require real-time communication
- [ ] Bigger applications in multiple files