login_query = """
    select * from user
    where id = %s and password = %s
"""

check_id_query = """
    select * from user
    where id = %s
"""

signup_query ="""
    insert into user
    where id =(%s,%s,%s)
"""

