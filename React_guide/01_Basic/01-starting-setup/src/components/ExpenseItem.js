import "./ExpenseItem.css";

// 관습상 파일 이름은 반복 사용됨
function ExpenseItem(props) {
  const month = props.date.toLocaleString("en-US", { month: "long" });
  const day = props.date.toLocaleString("en-US", { day: "2-digit" });
  const year = props.date.getFullYear(); // 4자리 수로 년도 추출

  return (
    <div className="expense-item">
      {/* <div>{props.date.toISOString()}</div> */}
      <div>
        <div>{month}</div>
        <div>{year}</div>
        <div>{day}</div>
      </div>
      <div className="expense-item__description">
        <h2>{props.title}</h2>
        <div className="expense-item__price">${props.amount}</div>
      </div>
    </div>
  );
} // 리액트 컴포넌트 안에 반환하는 코드(JSX)는 반드시 하나의 루트 요소를 가짐 -> div로 감싸기
// JSX는 결국 자바스크립트이므로 기존에 쓰던 html코드처럼 속성명 작성 x (ex. 'class=' -> 'className=')
// Class는 자바스크립트 예약어

export default ExpenseItem; // 컴포넌트를 내보냄
