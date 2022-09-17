import React, { useState } from "react";

import ExpenseDate from "./ExpenseDate";
import Card from "../UI/Card";
import "./ExpenseItem.css";

// function ExpenseItem(props) {
const ExpenseItem = (props) => {
  const [title, setTitle] = useState(props.title); // setTitle: 값을 업데이트하는 함수
  console.log("ExpenseItem evaluated by React"); // 컴포넌트가 호출될 때마다 인스턴스가 생성되므로 콘솔창에 호출 횟수만큼 찍힘

  const clickHandler = () => {
    setTitle("Updated!"); // title에 새로운 값을 할당하지 않는 이유: state의 업데이트를 예약함
  }; // 작명 방법 : 트리거 + 핸들러
  return (
    <Card className="expense-item">
      <ExpenseDate date={props.date} />
      <div className="expense-item__description">
        <h2>{title}</h2>
        <div className="expense-item__price">${props.amount}</div>
      </div>
      <button onClick={clickHandler}>Change Title</button>
    </Card>
  );
};

export default ExpenseItem;
