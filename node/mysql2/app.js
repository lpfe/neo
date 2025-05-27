const mysql = require('mysql2/promise');
const env = require('dotenv').config({ path: "../../.env" });

const db = async() => {
    try {
    let connection = await mysql.createConnection({
        host: process.env.host,
        user: process.env.user,
        port: process.env.port,
        password: process.env.password,
        database: process.env.database
    })



    let [rows, fields] = await connection.query('SELECT * FROM st_info');
    console.log(rows);

    let data = {
        st_id:"202499",
        name: "Moon",
        dept: "Computer"
    }

    let insertId = data.st_id;

        // insert query
        [rows, fields] = await connection.query("insert into st_info values ?", data);
        console.log("Data is inserted : " + insertId);

        // select for inserted query
        [rows. fields] = await connection.query("select * from st_info where st_id = ?", [insertId]);
        console.log(rows);

        // update query
        [rows, fields] = await connection.query("update st_info set dept = ? where st_id = ?", ["Game", insertId]);
        console.log("Data is updated : " + insertId);

        // select for updated query
        [rows. fields] = await connection.query("select * from st_info where st_id = ?", [insertId]);
        console.log(rows);

        // delete query
        [rows, fields] = await connection.query("delete st_info set dept = ? where st_id = ?", ["Game", insertId]);
        console.log("Data is deleted : " + insertId);

        // select for deleted query
        [rows. fields] = await connection.query("select * from st_info where st_id = ?", [insertId]);
        console.log(rows);

    } catch (error) {
        console.log(error);
    }

}

db();