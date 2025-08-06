import text
class Services:
    def get_job_result(self):
        try:

            with engine.connect() as connection:
                result=connection.excute(text("select * from table_name"))
                data=[dict(row) for row in result]
            return data
        except Exception as e:
            raise HTTPException(status_code=500, details="internal error")

    def get_job_search(self):
        try:

            with engine.connect() as connection:
                result=connection.excute(text("select * from table_name"))
                data=[dict(row) for row in result]
            return data
        except Exception as e:
            raise HTTPException(status_code=500, details="internal error")

    def get_job_salary(self):
        try:

            with engine.connect() as connection:
                result=connection.excute(text("select * from table_name"))
                data=[dict(row) for row in result]
            return data
        except Exception as e:
            raise HTTPException(status_code=500, details="internal error")