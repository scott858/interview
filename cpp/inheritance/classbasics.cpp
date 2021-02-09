#include <iostream>
#include <memory>

using namespace std;

class BBwidget {};
class BBslider : public BBwidget{};

class CWwidget {};
class CWslider : public CWwidget{};

class Ival_box {
public:
    virtual int get_value() = 0;

    virtual void set_value(int i) = 0;

    virtual void reset_value(int i) = 0;

    virtual void prompt() = 0;

    virtual bool was_changed() const = 0;

    virtual ~Ival_box() {}
};

class Ival_slider : public Ival_box {
public:
    Ival_slider(int ll, int hh) {};
    ~Ival_slider() override {};

    int get_value() override { return 0; };
    void prompt() override {cout << "hey\n";};

    void set_value(int i) override {};

    void reset_value(int i) override {};

    bool was_changed() const override {return true;};
};

class Ival_dial: public Ival_box {
public:
    Ival_dial(int ll, int hh) {};
    ~Ival_dial() override {};

    int get_value() override { return 0; };
    void prompt() override {cout << "hey base dial\n";};

    void set_value(int i) override {};

    void reset_value(int i) override {};

    bool was_changed() const override {return true;};
};

class BB_ival_slider : public Ival_slider, protected BBslider {
public:
    BB_ival_slider(int ll, int hh) : Ival_slider{0,0} {};
    ~BB_ival_slider() override {};

    int get_value() override { return 0; };
    void prompt() override {cout << "hey BB\n";};

    void set_value(int i) override {};

    void reset_value(int i) override {};

    bool was_changed() const override {return true;};
};

class CW_ival_slider : public Ival_slider, protected CWslider {
public:
    CW_ival_slider(int ll, int hh) : Ival_slider{0,0} {};
    ~CW_ival_slider() override {};

    int get_value() override { return 0; };
    void prompt() override {cout << "hey CW\n";};

    void set_value(int i) override {};

    void reset_value(int i) override {};

    bool was_changed() const override {return true;};
};

class BB_ival_dial : public Ival_dial, protected BBwidget {

public:
    BB_ival_dial(int hh, int ll) : Ival_dial(0,0) {};
    int get_value() override { return 0; };
    void prompt() override {cout << "hey BB dial\n";};

    void set_value(int i) override {};

    void reset_value(int i) override {};

    bool was_changed() const override {return true;};
};

class Flashing_ival_slider: public Ival_slider {
public:
    Flashing_ival_slider() : Ival_slider(0,0) {}
};

class Popup_ival_slider: public Ival_slider {
public:
    Popup_ival_slider() : Ival_slider(0,0) {}
};

class BB_flashing_ival_slider : public Flashing_ival_slider, protected BBslider {};

class BB_popup_ival_slider : public Popup_ival_slider, protected BBslider {};

class CW_flashing_ival_slider : public Flashing_ival_slider, protected CWslider {};

class CW_popup_ival_slider : public Popup_ival_slider, protected CWslider {
public:
    CW_popup_ival_slider() {};
};

class Ival_maker {
public:
    virtual Ival_dial * dial(int hh, int ll) = 0;
    virtual Popup_ival_slider * popup_slider(int hh, int ll) = 0;
};

class BBmaker : public Ival_maker {
public:
    Ival_dial * dial(int hh, int ll) override;
    Popup_ival_slider * popup_slider(int hh, int ll) override;
};

Ival_dial * BBmaker::dial(int hh, int ll) {
    return new BB_ival_dial{hh, ll};
}

Popup_ival_slider * BBmaker::popup_slider(int hh, int ll) {
    return new BB_popup_ival_slider{};
}

void user(Ival_maker &m) {
    unique_ptr<Ival_box> p {m.dial(0,0)};
    p->prompt();
}

int main() {
//    Ival_slider v_slider{0, 0};
    unique_ptr<Ival_slider> v_slider {new Ival_slider{0,0}};
    v_slider->prompt();

    unique_ptr<BB_ival_slider> bb_slider {new BB_ival_slider{0,0}};
    bb_slider->prompt();

    BBmaker bb_maker{};
    user(bb_maker);
    return 0;
}