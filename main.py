from config import *
from utils import *
from email_processing import *
from feature_extraction import * 
from models import *

# MENU 
def print_main_menu():
    print(Fore.MAGENTA + "")
    print(30 * "-", "MAIN MENU", 30 * "-")
    print(Style.RESET_ALL + "")
    print(Fore.GREEN + "1. Extracted Features")
    print(Fore.GREEN + "2. Machine Learning models")
    print(Fore.RED + "3. EXIT")
    print(Style.RESET_ALL + "")

def print_ml_models():
    print(30 * "*", "ML MODELS", 30 * "*")
    print(Fore.GREEN + "")
    print("1. Bagged Decision Tree")
    print("2. Random Forest")
    print("3. Extra Trees")
    print("4. Adaboost")
    print("5. Stochastic Gradient Boosting")
    print("6. Voting Ensemble")
    print("7. Naive Bayes")
    print("8. SVM")
    print(Fore.RED + "9. EXIT")
    print(Style.RESET_ALL + "")

# Main loop
def main():
    test_path = raw_input(Fore.BLUE + "Enter path of folder where mail is present: ")
    mail_files = get_files(test_path)
    features_list = extract_all_features_in_path(test_path, "?")

    loop = True
    while loop:
        print_main_menu()
        choice = input(Fore.BLUE + "Enter your choice: ")
        print(Fore.MAGENTA + "")

        if choice == 1:
            print("Feature Extraction")
            print("------------------")
            pprint.pprint(features_list, width=1)

        elif choice == 2:
            X_test = pd.DataFrame(features_list)
            del X_test['label']
            dfnew = X_test[['body_noFunctionWords', 'url_noIntLinks', 'body_richness', 'url_noLinks', 'url_linkText']]

            loop2 = True
            while loop2:
                print_ml_models()
                choice2 = input(Fore.BLUE + "Select the ML-model: ")
                print(Fore.MAGENTA + "")

                if choice2 == 1:
                    print("Prediction using Bagged Decision Tree Model")
                    y_pred = predict_with_model('bagged_decision_tree.pkl', dfnew)
                    print(Fore.BLUE)
                    print(y_pred)

                elif choice2 == 2:
                    print("Prediction using Random Forest Model")
                    y_pred = predict_with_model('random_forest.pkl', dfnew)
                    print(Fore.BLUE)
                    print(y_pred)

                elif choice2 == 3:
                    print("Prediction using Extra Trees Model")
                    y_pred = predict_with_model('extra_trees.pkl', dfnew)
                    print(Fore.BLUE)
                    print(y_pred)

                elif choice2 == 4:
                    print("Prediction using Adaboost Model")
                    y_pred = predict_with_model('adaboost.pkl', dfnew)
                    print(Fore.BLUE)
                    print(y_pred)

                elif choice2 == 5:
                    print("Prediction using Stochastic Gradient Boosting Model")
                    y_pred = predict_with_model('SGB.pkl', dfnew)
                    print(Fore.BLUE)
                    print(y_pred)

                elif choice2 == 6:
                    print("Prediction using Voting Ensemble Model")
                    y_pred = predict_with_model('voting_ensemble.pkl', dfnew)
                    print(Fore.BLUE)
                    print(y_pred)

                elif choice2 == 7:
                    print("Prediction using Naive Bayes Model")
                    y_pred = predict_with_model('naive_bayes.pkl', dfnew)
                    print(Fore.BLUE)
                    print(y_pred)

                elif choice2 == 8:
                    print("Prediction using SVM Model")
                    y_pred = predict_with_model('SVM.pkl', dfnew)
                    print(Fore.BLUE)
                    print(y_pred)

                elif choice2 == 9:
                    loop2 = False

                else:
                    raw_input("Wrong option selection. Enter any key to try again.")

        elif choice == 3:
            loop = False

        else:
            raw_input("Wrong option selection. Enter any key to try again.")

if __name__ == "__main__":
    main()