// import React from 'react'

// function User({ user }) {
//     return (
//         <div>
//             <b>{user.username}</b>
//             <span>{user.email}</span>
//         </div>
//     )
// }

// function UserList() {
//     const users = [
//         { id: 1, username: 'developer', email: 'public.developer@gmail.com' },
//         { id: 2, username: 'tester', email: 'public.tester@gmail.com' },
//         { id: 3, username: 'moon', email: 'public.moon@gmail.com' },
//     ];
//     return (
//         <div>
//             {
//                 users.map(user => (
//                     <User user={user} key={user.id} />
//                 ))
//             /* <div>
//                 <b>{users[0].username}</b>
//                 <span>{users[0].email}</span>
//             </div>
//             <div>
//                 <b>{users[1].username}</b>
//                 <span>{users[1].email}</span>
//             </div>
//             <div>
//                 <b>{users[2].username}</b>
//                 <span>{users[2].email}</span>
//             </div> */}
//         </div>
//     )
// }

// export default UserList;


import React, { useEffect } from 'react';

function User({ user, onRemove }) {
    useEffect(() => {
        console.log('user value setted...');
        console.log(user);
        return () => {
            console.log('before user value');
            console.log('uesr');
        }
    })
    return (
        <div>
            <b>{user.username}</b>-<span>{user.email}</span>
            <button onClick={() => onRemove(user.id)}>삭제</button>
        </div>
    )
}

function UserList({ users, onRemove }) {
    return (
        <div>
            {
                users.map(user => (
                    <User user={user} key={user.id} onRemove={onRemove} />
                ))
            }
        </div>
    )
}

export default UserList;