import 'package:flutter/material.dart';
import '../models/item_model.dart';
import '../services/data_service.dart';

class ItemProvider with ChangeNotifier {
  List<Item> _items = DataService.fetchItems();
  String _query = "";

  List<Item> get items {
    if (_query.isEmpty) return _items;
    return _items
        .where((item) =>
            item.title.toLowerCase().contains(_query.toLowerCase()))
        .toList();
  }

  void search(String query) {
    _query = query;
    notifyListeners();
  }
}