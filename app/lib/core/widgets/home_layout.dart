import 'package:flutter/material.dart';
import 'package:google_nav_bar/google_nav_bar.dart';
import '/core/util/themes.dart';
import '/features/realtime_object_detection/presentation/pages/realtime_object_detection_page.dart';

// ignore: must_be_immutable
class HomeLayout extends StatefulWidget {
  static const String routeName = 'HomePage';

  const HomeLayout({super.key});

  @override
  State<HomeLayout> createState() => _HomeLayoutState();
}

class _HomeLayoutState extends State<HomeLayout> {
  late double height;
  int selectedIndex = 0;
  late double width;

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: LayoutBuilder(builder: (context, BoxConstraints constraints) {
        return const Scaffold(
          resizeToAvoidBottomInset: false,
          body: RealTimeObjectDetectionPage(),
        );
      }),
    );
  }
}
