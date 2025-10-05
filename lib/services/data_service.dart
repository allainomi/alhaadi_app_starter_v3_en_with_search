import '../models/item_model.dart';

class DataService {
  static List<Item> fetchItems() {
    return [
      Item(title: "Flutter", description: "A framework for mobile apps."),
      Item(title: "Dart", description: "Programming language for Flutter."),
      Item(title: "Provider", description: "State management solution."),
      Item(title: "Firebase", description: "Backend as a service."),
    ];
  }
}