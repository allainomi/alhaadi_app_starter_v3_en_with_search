import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/item_provider.dart';
import '../widgets/item_card.dart';
import '../widgets/search_bar.dart';

class HomeView extends StatelessWidget {
  const HomeView({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => ItemProvider(),
      child: Scaffold(
        appBar: AppBar(title: const Text("AlHaadi App v3")),
        body: Column(
          children: [
            const SearchBarWidget(),
            Expanded(
              child: Consumer<ItemProvider>(
                builder: (context, provider, _) {
                  return ListView.builder(
                    itemCount: provider.items.length,
                    itemBuilder: (context, index) {
                      return ItemCard(item: provider.items[index]);
                    },
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}