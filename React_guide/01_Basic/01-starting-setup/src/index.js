import ReactDOM from "react-dom/client";

import "./index.css";
import App from "./App"; // 써드파티 라이브러리 or 내가 만든 js 파일이라면 .js는 생략 가능

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />); // JSX 구문
