import 'package:flutter/material.dart';
import 'core/widgets/home_layout.dart';
import 'core/util/themes.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AI App',
      theme: appTheme(),
      initialRoute: HomeLayout.routeName,
      home: const HomeLayout(),
    );
  }
}
