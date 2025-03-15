import CarbonGraph from "./components/CarbonGraph";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    socket.on("receive_data", (newData) => {
      setData((prev) => [...prev, newData].slice(-10)); // Store last 10 records
    });
  }, []);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-center text-2xl font-bold">Real-Time Carbon Tracker</h1>
      <CarbonGraph data={data} />
    </div>
  );
}