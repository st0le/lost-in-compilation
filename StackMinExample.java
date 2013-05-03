
public class StackMinExample {

	class Stack {
		private int[] stack;
		private int top;

		public Stack(int size) {
			this.stack = new int[size];
			this.top = -1;
		}

		public void push(int item) throws Exception {
			if (top == stack.length - 1)
				throw new Exception("Stack Capacity is full.");
			stack[++top] = item;
		}

		public boolean empty() {
			return top == -1;
		}

		public int peek() throws Exception {
			if (empty())
				throw new Exception("Stack is empty.");
			return stack[top];
		}

		public int pop() throws Exception {
			if (empty())
				throw new Exception("Stack is empty.");
			return stack[top--];
		}
	}

	class StackMin extends Stack {
		private Stack minStack;

		public StackMin(int size) {
			super(size);
			minStack = new Stack(size);
		}
		
		@Override
		public void push(int item) throws Exception {
			if(empty() || item <= minStack.peek())
				minStack.push(item);
			super.push(item);
		}
		
		@Override
		public int pop() throws Exception {
			int item = super.pop();
			if(item == minStack.peek())
				minStack.pop();
			return item;
		}
		
		public int min() throws Exception {
			if(empty()) throw new Exception("Stack is empty.");
			return minStack.peek();
		}

	}

	public static void main(String[] args) throws Exception {
		new StackMinExample().test();
	}

	private void test() throws Exception {
		StackMin stack = new StackMin(10);
		for (int item : new int[] { 67, 44, 20, 77, 99, 12 }) {
			stack.push(item);
			System.out.printf("Pushing %d, Minimum : %d\n", item, stack.min());
		}
		while (!stack.empty()) {
			System.out
					.printf("Pop : %d\n", stack.pop());
			if(!stack.empty())
				System.out.printf("Minimum : %d\n",stack.min());
		}
	}
}