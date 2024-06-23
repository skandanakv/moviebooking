import sqlite3

def MovieData():
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, Movie_ID text, Movie_Name text, Release_Date text, Director text, Cast text, Budget text, Duration text, Rating text)")
    con.commit()
    con.close()

def AddMovieRec(Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating):
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating))
    con.commit()
    con.close()

def ViewMovieData():
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    con.close()
    return rows

def DeleteMovieRec(id):
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    con.commit()
    con.close()

# def SearchMovieData(Movie_ID="", Movie_Name="", Release_Date="", Director="", Cast="", Budget="", Duration="", Rating=""):
#     con = sqlite3.connect("movie1.db")
#     cur = con.cursor()
#     cur.execute("SELECT * FROM book WHERE Movie_ID=? OR Movie_Name=? OR Release_Date=? OR Director=? OR Cast=? OR Budget=? OR Duration=? OR Rating=?", (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating))
#     rows = cur.fetchall()
#     con.close()
#     return rows


def SearchMovieData(Movie_ID="", Movie_Name="", Release_Date="", Director="", Cast="", Budget="", Duration="",
                    Rating=""):
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()

    # Build the SQL query based on provided parameters
    query = "SELECT * FROM book WHERE 1=1"  # Initial query

    # Check each parameter and append to the query if not empty
    if Movie_ID:
        query += " AND Movie_ID LIKE ?"
    if Movie_Name:
        query += " AND Movie_Name LIKE ?"
    if Release_Date:
        query += " AND Release_Date LIKE ?"
    if Director:
        query += " AND Director LIKE ?"
    if Cast:
        query += " AND Cast LIKE ?"
    if Budget:
        query += " AND Budget LIKE ?"
    if Duration:
        query += " AND Duration LIKE ?"
    if Rating:
        query += " AND Rating LIKE ?"

    cur.execute(query, (
    '%' + Movie_ID + '%', '%' + Movie_Name + '%', '%' + Release_Date + '%', '%' + Director + '%', '%' + Cast + '%',
    '%' + Budget + '%', '%' + Duration + '%', '%' + Rating + '%'))
    rows = cur.fetchall()
    con.close()

    return rows


def UpdateMovieData(id, Movie_ID="", Movie_Name="", Release_Date="", Director="", Cast="", Budget="", Duration="", Rating=""):
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute("UPDATE book SET Movie_ID=?, Movie_Name=?, Release_Date=?, Director=?, Cast=?, Budget=?, Duration=?, Rating=? WHERE id=?", (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating, id))
    con.commit()
    con.close()