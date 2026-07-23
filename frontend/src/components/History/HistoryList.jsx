import HistoryCard from "./HistoryCard";
import EmptyHistory from "./EmptyHistory";

const HistoryList = ({ history, onDelete }) => {
  if (history.length === 0) {
    return <EmptyHistory />;
  }

  return (
    <div className="grid gap-5">
      {history.map((item) => (
        <HistoryCard
          key={item.id}
          item={item}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
};

export default HistoryList;