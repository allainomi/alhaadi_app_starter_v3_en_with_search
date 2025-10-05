import 'package:flutter/material.dart';
import 'views/home_view.dart';
import 'core/theme.dart';

void main() {
  runApp(const AlHaadiApp());
}

class AlHaadiApp extends StatelessWidget {
  const AlHaadiApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AlHaadi Starter v3',
      theme: appTheme,
      home: const HomeView(),
      debugShowCheckedModeBanner: false,
    );
  }
}