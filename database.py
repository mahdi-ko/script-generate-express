def database_connect():
    return """
const { Sequelize } = require("sequelize")
const db = new Sequelize(
    process.env.DB_NAME,
    process.env.DB_USERNAME,
    process.env.DB_PASSWORD,
    {
        define: {
            charset: "utf8",
            collate: "utf8_general_ci",
        },
        host: process.env.DB_HOST,
        port: process.env.DB_PORT,
        dialect: "mysql",
        logging: false,
        pool: {
            max: 100000,
        },
    }
);
//this thing is a function that executes itself
(async () => {
    try {
        await db.authenticate();
        console.log("db connected");
    } catch (err) {
        console.log(err);
    }
})();

module.exports = db;
"""
