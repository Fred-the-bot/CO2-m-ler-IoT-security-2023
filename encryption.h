int prime=29;
int generator=3;
int client_key=15;
int server_key=19;

unsigned long long client_full_key=pow(server_key,client_key);
int client_full_key=client_full_key%29
