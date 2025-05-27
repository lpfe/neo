// import React from "react";
// // import Hello from "./Hello";
// // import './App.css';
// // import Wrapper from './Wrapper'
// // import Counter from './Counter';
// // import InputSample from './InputSample';
// import User from './UserList';


// function App() {
//   return <User />;
// }

// export default App;




// --------------------------------

// import React, { useRef } from "react";
// import UserList from './UserList';
// import CreateUser from "./CreateUser";

// function App() {
//   const users = [
//     { id: 1, username: 'developer', email: 'public.developer@gmail.com' },
//     { id: 2, username: 'tester', email: 'public.tester@gmail.com' },
//     { id: 3, username: 'moon', email: 'public.moon@gmail.com' },
//   ];

//   const nextId = useRef(4);
//   const OnCreate = () => {
//     nextId.current += 1;
//   }
//   return (
//     <>
//       <CreateUser />
//       <UserList users={users} />
//     </>
//   )
// }

// export default App;



// ---------------------------------


import React, { useRef, useState, useMemo } from "react";
import UserList from './UserList';
import CreateUser from "./CreateUser";

function countActiveUsers(users) {
  console.log('활성 사용자 수를 세는 중...')
  return users.filter(user => user.active).length
}

function App() {
  const [inputs, setInputs] = useState({
    username: '',
    email: '',
  })

  const { username, email } = inputs;

  const onChange = e => {
    const { name, value } = e.target;
    setInputs({
      ...inputs,
      [name]: value,
    })
  }

  const [users, setUsers] = useState([
    { id: 1, username: 'developer', email: 'public.developer@gmail.com' },
    { id: 2, username: 'tester', email: 'public.tester@gmail.com' },
    { id: 3, username: 'moon', email: 'public.moon@gmail.com' },
  ]);

  const nextId = useRef(4);
  const onCreate = () => {
    const user = {
      id: nextId.current,
      username,
      email,
    }
    setUsers(users.concat(user));

    setInputs({
      username: '',
      email: '',
    })
    nextId.current += 1;
  }
  const onRemove = id => {
    setUsers(users.filter(user => user.id !== id));
  };

  const count = useMemo(() => countActiveUsers(users), [users])

  return (
    <>
      <CreateUser username={username} email={email} onChange={onChange} onCreate={onCreate} />
      <UserList users={users} onRemove={onRemove} />
      <div>활성 사용자 수 : {count}</div>
    </>
  )
}

export default App;