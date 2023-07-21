import db from '../config/db.js';

export const register = async({first_name, last_name, username, email, hash}) => {
    const trx = await db.transaction();
    try {
        const user = await db('users')
        .insert({
            first_name,
            last_name,
            username,
            email,
            last_login: new Date()
        }, ["user_id", "username", "email", "first_name", "last_name"]).transacting(trx);

        console.log('user=>', user);

        const login = await db('login')
        .insert({
            username: user.username || username,
            password: hash
        }, ["login_id", "username", "password"])
        .transacting(trx);

        console.log('login=>', login);
        await trx.commit();
        return user;
    } catch (err) {
        console.log('err=>', err);
        await trx.rollback();
        throw new Error(err.message);
    }
};