import 'package:flutter/material.dart';
import '../models/item_model.dart';

class ItemCard extends StatelessWidget {
  final Item item;
  const ItemCard({super.key, required this.item});

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.symmetric(vertical: 5, horizontal: 12),
      child: ListTile(
        title: Text(item.title),
        subtitle: Text(item.description),
        trailing: const Icon(Icons.arrow_forward_ios),
      ),
    );
  }
}