import 'package:flutter_test/flutter_test.dart';

void main() {
  test('Basic arithmetic test', () {
    expect(1 + 1, 2);
    expect(2 * 3, 6);
  });

  test('List test', () {
    List<String> names = ['Alice', 'Bob', 'Charlie'];
    expect(names.length, 3);
    expect(names.contains('Alice'), true);
  });

  testWidgets('Widget test without specific app', (WidgetTester tester) async {
    // A simple container test
    await tester.pumpWidget(
      MaterialApp(
        home: Scaffold(
          body: Container(
            child: Text('Hello World'),
          ),
        ),
      ),
    );

    expect(find.text('Hello World'), findsOneWidget);
  });
}
