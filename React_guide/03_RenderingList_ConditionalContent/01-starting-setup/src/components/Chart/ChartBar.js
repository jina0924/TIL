import React from "react";

import "./ChartBar.css";

const ChartBar = (props) => {
  let barFillHeight = "0%";

  if (props.max > 0) {
    barFillHeight = Math.round((props.value / props.maxValue) * 100) + "%";
  }

  return (
    <div className="chart-bar">
      <div className="chart-bar__inner">
        <div
          className="chart-bar__fill"
          // style={{ height: barFillHeight, backgroundColor: "red" }}
          style={{ height: barFillHeight }}
        ></div>
      </div>
      <div className="chart-bar__label">{props.label}</div>
    </div>
  );
  // 스타일 지정 방법: 속성 이름에 '-' 들어가면 속성 이름을 따옴표로 감싸줘야 함 or camelCase로 작성해야 함
};

export default ChartBar;
