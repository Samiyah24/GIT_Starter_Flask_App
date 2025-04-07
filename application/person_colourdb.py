import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="get_into_tech_c2_2025"
)


def main():
  print(mydb)

  cursor = mydb.cursor()

  sql = "INSERT INTO person_2 (firstname, lastname, flowerid) VALUES (%s, %s, %s)"
  val = ("Aiman", "TBC", 3)
  cursor.execute(sql, val)

  mydb.commit()

  print(cursor.rowcount, "record inserted.")


def get_db_connection():
  mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="get_into_tech_c2_2025"
  )
  return mydb


def get_people():
    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL query to join person and colour tables
    sql = """
    SELECT person_2.PersonID, person_2.Firstname, person_2.Lastname, Flowers.Name AS FlowerName
    FROM person_2
    JOIN flowers ON person_2.FlowerID = flowers.FlowerID
    """

    cursor.execute(sql)

    result_set = cursor.fetchall()
    person_list = []
    for person in result_set:
        person_list.append({
            'PersonID': person[0],
            'Firstname': person[1],
            'Lastname': person[2],
            'FlowerName': person[3]  #
        })
    return person_list


def update_person(person_id, new_lastname, new_flowerid):
    # Establish connection to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL query to update the person record
    sql = "UPDATE person_2 SET Lastname = %s, FlowerID = %s WHERE PersonID = %s"

    val = (new_lastname, new_flowerid, person_id)

    # Execute the query with the provided values
    cursor.execute(sql, val)

    # Commit the transaction to save changes in the database
    conn.commit()

    # Optionally, print how many rows were affected
    print(cursor.rowcount, "record(s) updated.")


if __name__ == "__main__":
  main()