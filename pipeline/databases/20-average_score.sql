-- creates a procedure to compute the average score for user
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id_new INTEGER)
BEGIN
	UPDATE users SET average_score=(
	SELECT AVG(score) FROM corrections WHERE user_id=user_id_new)
	WHERE id=user_id_new;
END; //
DELIMITER ;