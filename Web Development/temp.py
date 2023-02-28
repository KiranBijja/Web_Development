from flask import Flask, request
import mysql.connector

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]

        if not name or not surname:
            return """
            <html>
                <body>
                    <form method="get">
                    <h3>Both Name and Surname fields are required!</h3>
                        <input type="submit" value="Back">
                    </form>
                </body>
            </html>
            """
        # Connect to the database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="users",
            auth_plugin="mysql_native_password"
        )
        cursor = conn.cursor()

        # Insert the data into the database
        sql = "INSERT INTO users (name, surname) VALUES (%s, %s)"
        val = (name, surname)
        cursor.execute(sql, val)
        conn.commit()

        return """
        <html>
            <body>
            <form method="get">
            <h3>Data inserted successfully!</h3>
            <input type="submit" value="Home">
            </form>
        </html>
        """
    else:
        return """
            <html>
            <body>
                <form method="post">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name"><br><br>
                    <label for="surname">Surname:</label>
                    <input type="text" id="surname" name="surname"><br><br>
                    <input type="submit" value="Submit">
                </form>
            </body>
            </html>
        """


if __name__ == "__main__":
    app.run()

