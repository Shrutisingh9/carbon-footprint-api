import { Line } from "react-chartjs-2";

function CarbonGraph({ data }) {
  const chartData = {
    labels: data.map((_, index) => Minute ${index + 1}),
    datasets: [{ label: "Carbon Footprint (kg)", data, borderColor: "green", fill: false }],
  };

  return <Line data={chartData} />;
}

export default CarbonGraph;