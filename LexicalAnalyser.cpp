#include<bits/stdc++.h>
#include<regex>
using namespace std;

vector<char> punctuations = {' ', '+', '-', '*', '/', ',', ';', '>', '<', '=', '(', ')', '[', ']', '{', '}', '&', '|', '\n','"','!','$'};
vector<char> digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
vector<char> operators = {'+', '-', '*', '/', '>', '<', '=', '|', '&'};
vector<string> keywords = { "as", "constant", "enum", "if",
        "overload", "subrange", "type",
        "case", "continue", "exit", "import", "proc", "switch", "while",
        "cast", "do", "for", "in",
        "repeat", "to", "with",
        "break", "exit", "goto", "new", "return", "begin", "end", "if", "package","global", "is", "private", "undef", "by", "else","iterator","integer", "public", "untyped","local","main","then","const"};


map<string, int> Identifiers;
map<string, int> Numbers;
map<string, int> Keywords;
map<string, int> WrongStr;
map<char, int> Operators;

bool isdigit(char ch){
   
   regex digitPattern("[0-9]");
    return regex_match(string(1, ch), digitPattern);
  
}
bool validIdentifier(string str)			
{
    if (isdigit(str[0])==true || find(punctuations.begin(), punctuations.end(), str[0]) != punctuations.end()){
        return false;
    }								
    
int len = str.size();
    if(len == 1){
        return true;
    }
  							
    else{
    	for (int i = 1 ; i < len ; i++)				
    	{
        	if (find(operators.begin(), operators.end(), str[i]) != operators.end()){
            	return false;
        	}
    	}
    }
    return true;
}

bool isNumber(const string &str) {
    regex numberPattern("^-?[0-9]+(\\.[0-9]+)?([eE][-+]?[0-9]+)?$");
    return regex_match(str, numberPattern);
}
void processLexeme(string str)						
{
    int left = 0;
	int right = 0;
    int len = str.size();
    while(right <= len && left <= right) {
        if(find(punctuations.begin(), punctuations.end(), str[right]) == punctuations.end()){
                right++;
        }
        if(find(punctuations.begin(), punctuations.end(), str[right]) != punctuations.end() && left == right){
        
            if(find(operators.begin(), operators.end(), str[right]) != operators.end()){
				Operators[str[right]]++;
                
            }
            right++;
            left = right;
        } 
       else if(find(punctuations.begin(), punctuations.end(), str[right]) != punctuations.end() && left != right || (right == len && left != right)){
          
        string sub=str.substr(left,right-left);
	if(find(keywords.begin(), keywords.end(), sub) != keywords.end()){
	
	      Keywords[sub]++;
				
           }
        else if(isNumber(sub) == true){
		
		  Numbers[sub]++;
				
			}
        else if(validIdentifier(sub) == true){
				
		Identifiers[sub]++;
				
		}
            else if(validIdentifier(sub) == false){
			
			WrongStr[sub]++;
				
			}
            left = right;
        }
    }
    return;
}
void printOperators() {
    cout << "Number of Operators Encountered : " << Operators.size() << "\n";
    for (auto x : Operators) {
        cout << x.first << " : " << x.second << "\n";
    }
}

void printKeywords() {
    cout << "\nNumber of Keywords Encountered : " << Keywords.size() << "\n";
    for (auto x : Keywords) {
        cout << x.first << " : " << x.second << "\n";
    }
}

void printNumbers() {
    cout << "\nNumber of Numbers Encountered : " << Numbers.size() << "\n";
    for (auto x : Numbers) {
        cout << x.first << " : " << x.second << "\n";
    }
}

void printIdentifiers() {
    cout << "\nNumber of Identifiers Encountered : " << Identifiers.size() << "\n";
    for (auto x : Identifiers) {
        cout << x.first << " : " << x.second << "\n";
    }
}

void printWrongLexemes() {
    cout << "\nNumber of Wrong Lexemes Encountered : " << WrongStr.size() << "\n";
    for (auto x : WrongStr) {
        cout << x.first << " : " << x.second << "\n";
    }
}

void printParsedMessage() {
    cout << "\nSuccessfully Parsed \"lab2.sd7\"\n";
}
 
int main(int argc, char* argv[]){
	string SeedString;
	auto ss = ostringstream{};
	ifstream Seed7File(argv[1]);
	ss << Seed7File.rdbuf();
	SeedString = ss.str();
	processLexeme(SeedString);
	
	printOperators();
	printKeywords();
	printNumbers();
	printIdentifiers();
        printWrongLexemes();
        printParsedMessage();
	return 0;
}
