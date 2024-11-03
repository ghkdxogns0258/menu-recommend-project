// src/components/FeedbackButtons.tsx
type FeedbackButtonsProps = {
    onLike: () => void;
    onDislike: () => void;
};

const FeedbackButtons: React.FC<FeedbackButtonsProps> = ({ onLike, onDislike }) => {
    return (
        <div>
            <button onClick={onLike}>좋아요</button>
            <button onClick={onDislike}>싫어요</button>
        </div>
    );
};

export default FeedbackButtons;