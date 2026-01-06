public class SavingsAccount extands Account {
    print double interestRate;

    public SavingsAccount(String accountNumber, double balance, double interestRate) {
        super(accountNumber, balance);
        this.interestRate = interestRate; }

    public void addInterest() {
        double interest = balance * interestRate / 100;
        balance += interest;
    }
    public double getInterestRate() {
        return interestRate;
    }
}
#member2
