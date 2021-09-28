import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.control.Button;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;
import javafx.geometry.Insets;

/**
 * GUI program to simulate a color game.
 * @author spanag3
 * @version 11.0.9.1
 */
public class ColorGame extends Application {
    private String x;
    private int scoreNum = 0;
    private Label score = new Label("Score: " + scoreNum);
    private boolean keepGoing = true;
    private String[] checker = new String[6];
    private Label lab = new Label("Name: None");
    private Label toBegin = new Label("Choose an answer to begin!");
    private TextField nameGiven = new TextField();
    /**
     * Method to start the layout.
     * @param primaryStage the stage for the GUI
     */
    public void start(Stage primaryStage) {
        BorderPane pane = new BorderPane();
        VBox use = getVboxTop();
        pane.setTop(use);
        pane.setBottom(getVboxBot());
        Scene scene = new Scene(pane, 500, 300);
        primaryStage.setTitle("Color Game!");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    /**
     * Method that creates the first row with the name.
     * @return a vbox to place inside pane.
     */
    private VBox getVboxTop() {
        VBox name = new VBox(15);
        HBox inside = new HBox(5);
        name.setPadding(new Insets(10, 10, 15, 15));
        Button enter = new Button("Enter");
        name.getChildren().addAll(lab);
        inside.setPadding(new Insets(10, 10, 15, 15));
        inside.getChildren().addAll(nameGiven, enter);
        name.getChildren().add(inside);

        //Actions
        enter.setOnAction(e -> {
            x = (nameGiven.getText());
            lab.setText("Name: " + x);
        });

        return name;
    }

    /**
     * Method to place the second VBox with the answers.
     * @return a vbox to place on the bottom of the pane
     */
    private VBox getVboxBot() {
        Button firstName = new Button();
        Button secondName = new Button();
        Button thirdName = new Button();
        Button questionBoxBut = new Button();
        changeContents(firstName, secondName, thirdName, questionBoxBut);
        Button resetButton = new Button("Reset");
        Button noneButton = new Button("None");

        HBox scoreRep = new HBox(5);
        scoreRep.getChildren().add(score);
        VBox colorAnswers = new VBox(2);
        colorAnswers.setPadding(new Insets(10, 10, 15, 15));
        HBox answerChoices = new HBox(5);
        answerChoices.setPadding(new Insets(10, 10, 15, 15));
        HBox questionBox = new HBox(85);
        questionBox.setPadding(new Insets(10, 10, 15, 15));
        questionBox.getChildren().addAll(questionBoxBut, resetButton);
        answerChoices.getChildren().addAll(firstName, secondName, thirdName, noneButton);
        HBox begin = new HBox(5);
        begin.getChildren().add(toBegin);
        colorAnswers.getChildren().addAll(scoreRep, questionBox, answerChoices, begin);

        //Actions
        firstName.setOnAction(e -> {
            if (checker[0].equals(checker[3])) {
                scoreNum += 1;
                score.setText("Score: " + scoreNum);
                toBegin.setText("Correct!");
                changeContents(firstName, secondName, thirdName, questionBoxBut);
            } else {
                scoreNum = 0;
                toBegin.setText("Incorrect");
            }
        });

        secondName.setOnAction(e -> {
            if (checker[1].equals(checker[4])) {
                scoreNum += 1;
                score.setText("Score: " + scoreNum);
                toBegin.setText("Correct!");
                changeContents(firstName, secondName, thirdName, questionBoxBut);
            } else {
                scoreNum = 0;
                toBegin.setText("Incorrect");
            }
        });

        thirdName.setOnAction(e -> {
            if (checker[2].equals(checker[5])) {
                scoreNum += 1;
                score.setText("Score: " + scoreNum);
                toBegin.setText("Correct!");
                changeContents(firstName, secondName, thirdName, questionBoxBut);
            } else {
                scoreNum = 0;
                toBegin.setText("Incorrect");
            }
        });

        noneButton.setOnAction(e -> {
            if (!checker[2].equals(checker[5]) && !checker[1].equals(checker[4]) && !checker[0].equals(checker[3])) {
                scoreNum += 1;
                score.setText("Score: " + scoreNum);
                toBegin.setText("Correct!");
                changeContents(firstName, secondName, thirdName, questionBoxBut);
            } else {
                scoreNum = 0;
                toBegin.setText("Incorrect");
            }
        });

        resetButton.setOnAction(e -> {
            lab.setText("Name: None");
            toBegin.setText("Choose an answer to begin!");
            scoreNum = 0;
            score.setText("Score: " + scoreNum);
            nameGiven.clear();
            changeContents(firstName, secondName, thirdName, questionBoxBut);
        });
        return colorAnswers;
    }
    /**
     * Method that changes the buttons and randomizes their colors.
     * @param one the first answer choice button button
     * @param two the second answer choice button
     * @param three the third answer choice button
     * @param fr the questinon box button
     */
    public void changeContents(Button one, Button two, Button three, Button fr) {
        String[] colorNames = {"red", "orange", "yellow", "green", "purple"};
        String questionBoxName = colorNames[(int) Math.floor(Math.random() * (3 - 0 + 1))];
        String questionBoxFill = colorNames[(int) Math.floor(Math.random() * (3 - 0 + 1))];
        String randomName1 = colorNames[(int) Math.floor(Math.random() * (3 - 0 + 1))];
        String randomName2 = colorNames[(int) Math.floor(Math.random() * (3 - 0 + 1))];
        String randomName3 = colorNames[(int) Math.floor(Math.random() * (3 - 0 + 1))];
        String randomFill1 = colorNames[(int) Math.floor(Math.random() * (3 - 0 + 1))];
        String randomFill2 = colorNames[(int) Math.floor(Math.random() * (3 - 0 + 1))];
        String randomFill3 = colorNames[(int) Math.floor(Math.random() * (3 - 0 + 1))];

        checker[0] = randomName1;
        checker[1] = randomName2;
        checker[2] = randomName3;
        checker[3] = randomFill1;
        checker[4] = randomFill2;
        checker[5] = randomFill3;

        one.setText(randomName1);
        two.setText(randomName2);
        three.setText(randomName3);
        fr.setText(questionBoxName);
        one.setStyle(String.format("−fx−background−color: %s; -fx-border-color: %s;", randomFill1, randomFill1));
        two.setStyle(String.format("−fx−background−color: %s; -fx-border-color: %s;", randomFill2, randomFill2));
        three.setStyle(String.format("−fx−background−color: %s; -fx-border-color: %s;", randomFill3, randomFill3));
        fr.setStyle(String.format("−fx−background−color: %s; -fx-border-color: %s;", questionBoxFill, questionBoxFill));
    }
}
